# predictionsgrader
for grading machine learning predictions

Program runs on pandas python library

=============================================================
             How to use PredictionsGrader  
=============================================================


The program contains two classes
1. PredictionsGrader
2. PredictionsGraderCSV


========================
PredictionsGrader class
========================

This compares two columns. The files are expected to be the predictions gotten in the submitted column and the predictions
stated in the confirmatory column.
It takes in the two columns to be compared as arguments to it's initializer in the order of submitted column first, then
confirmatory column next.
It supports two methods:
grade() and get()

The grade() method performs the comparing. It has parameter "return_as" that tells the method how to store the
comparation. It's values can be any of the following:
- true/false
- correct/wrong
- 1/0
- hit/miss

The get() method tells the class how to return the result. Either as data format or percentages.
It takes in the "format" parameter with value of "data" and returns a dataframe object else, it
returns the percentages of matched to unmatched.

Use Case:
        grade = PredictionsGrader(y_predictions, y_target).grade(return_as="1/0").get(format="data")
        print(grade)



===========================
PredictionsGraderCSV class
===========================
This compares two csv files.
It takes in the two files to be compared as arguments to it's initializer in the order of predictions file first, then
confirmatory file next.
It has the compare() method where you specify which two columns to compare and the grade() method to grade the truth or false
values. This grade method works exactly like that in the PredictionsGrader class.
It's get() method is the same as above.
It however possesses an extra method: get_csv which creates a csv file for you.

It takes in three arguments - filename (the name of the file to be created), append_to (the name of the column to append in the created file),
and predictions_name (the name to use in saving your predictions)


Use Case:
        grade = PredictionsGraderCSV(submission, answer).compare('Survived', 'Survived').grade().get(format="data")
        OR
        grade = PredictionsGraderCSV(submission, answer).compare('Survived', 'Survived').grade().get_csv(filename="Project Prediction.csv", append_to="Id", predictions_name="my predictions")