"""
    @ Author: Kenechukwu Agbo, (Kaggle - @Xceptions)
"""

import pandas as pd


class PredictionsGrader():
    '''
        Class compares two dataframe columns
    '''
    def __init__(self, predictions, target):
        self.correct = []
        self.predictions = predictions
        self.target = target


    def grade(self, return_as=""):
        # decide what values to use for representing matches
        if (return_as == "correct/wrong"):
            self.truth = "Correct"
            self.false = "Wrong"
        elif (return_as == "true/false"):
            self.truth = "True"
            self.false = "False"
        elif (return_as == "1/0"):
            self.truth = "1"
            self.false = "0"
        else:
            self.truth = "Hit"
            self.false = "Miss"

        # create the matches list
        for x in range(len(self.predictions)):
            if (self.predictions[x] == self.target[x]):
                self.correct.append(self.truth)
            else:
                self.correct.append(self.false)
        return self


    # decide if to return the data or percentages
    def get(self, format=""):
        if (format == "data"):
            return self.correct
        else:
            accurate = (self.correct.count(self.truth) / len(self.correct))
            unaccurate = 1 - accurate
        return("matched: {}, unmatched {}".format(accurate, unaccurate))



class PredictionsGraderCSV():
    '''
        This class is used for comparing csv files
    '''

    def __init__(self, predictions_file, target_file):
        self.correct = []
        self.predictions_file = pd.read_csv(predictions_file)
        self.target_file = pd.read_csv(target_file)


    def compare(self, predicted_target, confirmed_target):
        # specify the columns to compare
        self.predicted_target = self.predictions_file[predicted_target]
        self.confirmed_target = self.target_file[confirmed_target]
        return self


    def grade(self, return_as=""):
        if (return_as == "correct/wrong"):
            self.truth = "Correct"
            self.false = "Wrong"
        elif (return_as == "true/false"):
            self.truth = "True"
            self.false = "False"
        elif (return_as == "1/0"):
            self.truth = "1"
            self.false = "0"
        else:
            self.truth = "Hit"
            self.false = "Miss"

        for x in range(len(self.predicted_target)):
            if (self.predicted_target[x] == self.confirmed_target[x]):
                self.correct.append(self.truth)
            else:
                self.correct.append(self.false)
        return self


    def get(self, format=""):
        if (format == "data"):
            return self.correct
        else:
            accurate = (self.correct.count(self.truth) / len(self.correct))
            unaccurate = 1 - accurate
            return("matched: {}, unmatched {}".format(accurate, unaccurate))
        return self


    def get_csv(self, filename="", append_to="", predictions_name=""):
        self.append_to = self.predictions_file[append_to]
        self.submission = pd.DataFrame({append_to: self.append_to, predictions_name: self.correct})
        self.filename = filename
        self.submission.to_csv(self.filename, index=False)
        return ("file saved as {}".format(self.filename))
