def model_fit_quality(training_accuracy, test_accuracy):
    if training_accuracy > 1.2 * test_accuracy:
        return 1
    if training_accuracy <= 0.7 and test_accuracy <= 0.7:
        return -1
    return 0


print(model_fit_quality(training_accuracy=0.95, test_accuracy=0.65))
