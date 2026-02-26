from django.db import models

# This Student Performance Prediction app uses Machine Learning
# for predictions without requiring database models.
# The ML model (scikit-learn) handles all predictions via views.py
# No database persistence is needed for real-time predictions.

# Future enhancement: You could add a PredictionHistory model
# to store past predictions for analytics purposes.

# class PredictionHistory(models.Model):
#     study_hours = models.FloatField()
#     attendance = models.FloatField()
#     previous_score = models.FloatField()
#     sleep_hours = models.FloatField()
#     sample_papers = models.IntegerField()
#     predicted_score = models.FloatField()
#     grade = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Prediction: {self.predicted_score} ({self.grade})'
