#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x9af896e6

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

import csv
import os.path
from pprint import pprint

import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.optimizers import SGD
from keras.utils import to_categorical

# Data processing:

data_file = os.path.join(os.path.dirname(__file__), "house_votes.csv")

X = []
y = []
with open(data_file, "r") as house_votes:
    for row in csv.reader(house_votes):
        target, features = row[0], row[1:]
        def _coconut_lambda_0(_=None):
            raise TypeError("unknown party %r" % _)
        (y.append)(((lambda _=None: 1 if _ == "democrat" else 0 if _ == "republican" else (_coconut_lambda_0)(_)))(target))
        def _coconut_lambda_1(_=None):
            raise TypeError("unknown vote %r" % _)
        (X.append)((list)(map(lambda _=None: 1 if _ == "y" else -1 if _ == "n" else 0 if _ == "?" else (_coconut_lambda_1)(_), features)))

y = (to_categorical)(y)
X = (np.asarray)(X)

train_split = (int)(.6 * len(X))
validate_split = (int)(train_split + .2 * len(X))

X_train, X_validate, X_test = X[:train_split], X[train_split:validate_split], X[validate_split:]
y_train, y_validate, y_test = y[:train_split], y[train_split:validate_split], y[validate_split:]

# BBOpt setup:

from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__, pretty_json=False)

try:
    N = int(sys.argv[1])
except Exception:
    N = 5

for i in bb.loop(n=N, backend="scikit-optimize"):

# Main program:

    print("\n= %d =" % i)

    model = Sequential()

    hidden_neurons = bb.randint("hidden neurons", 1, 10, guess=2)

    model.add(Dense(units=hidden_neurons, input_dim=len(X_train[0])))
    model.add(Activation("relu"))
    model.add(Dense(units=2))
    model.add(Activation("softmax"))

    model.compile(loss="categorical_crossentropy", optimizer=SGD(lr=bb.uniform("learning rate", 0, 0.2, guess=0.01), momentum=bb.uniform("momentum", 0, 1, guess=0.9), nesterov=(bool)(bb.randint("nesterov", 0, 1, guess=1)), decay=bb.uniform("decay", 0, 0.1, guess=0.001)), metrics=["accuracy"])

    train_history = model.fit(X_train, y_train, epochs=100, batch_size=bb.randint("batch size", 1, 32, guess=16), verbose=0)

    pprint(bb.get_current_run())

    train_loss, train_acc = train_history.history["loss"][-1], train_history.history["acc"][-1]
    print("training loss = %r\ntraining accuracy = %r" % (train_loss, train_acc))

    validation_loss, validation_acc = model.evaluate(X_validate, y_validate, verbose=0)
    print("validation loss = %r\nvalidation accuracy = %r" % (validation_loss, validation_acc))

    bb.minimize(validation_loss)

    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print("test loss = %r\ntest accuracy = %r" % (test_loss, test_acc))

    bb.remember({"training loss": train_loss, "training accuracy": train_acc, "validation loss": validation_loss, "validation accuracy": validation_acc, "test loss": test_loss, "test accuracy": test_acc})

print("\n= BEST =")
pprint(bb.get_optimal_run())
