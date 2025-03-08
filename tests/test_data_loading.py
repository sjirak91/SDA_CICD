import sys
import os
import pytest

# Add the project root directory to the system path for all tests
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from data_loading import load_and_process_data


def test_data_loading():
    X_train, X_test, y_train, y_test = load_and_process_data()
    assert X_train.shape[0] > 0
    assert X_test.shape[0] > 0
