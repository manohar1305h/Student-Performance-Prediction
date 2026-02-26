import numpy as np
import os
import joblib
from django.shortcuts import render
from django.conf import settings


def get_grade(score):
    """Convert score to grade."""
    if score >= 90:
        return 'A+ (Outstanding)'
    elif score >= 80:
        return 'A (Excellent)'
    elif score >= 70:
        return 'B (Good)'
    elif score >= 60:
        return 'C (Average)'
    elif score >= 50:
        return 'D (Below Average)'
    else:
        return 'F (Fail)'


def get_performance_color(score):
    """Return a color class based on score."""
    if score >= 80:
        return 'success'
    elif score >= 60:
        return 'warning'
    else:
        return 'danger'


def home(request):
    """Render the prediction form."""
    return render(request, 'predictor/home.html')


def predict(request):
    """Handle form submission and predict student performance."""
    if request.method == 'POST':
        try:
            # Get form data
            study_hours = float(request.POST.get('study_hours', 0))
            attendance = float(request.POST.get('attendance', 0))
            previous_score = float(request.POST.get('previous_score', 0))
            sleep_hours = float(request.POST.get('sleep_hours', 0))
            sample_papers = int(request.POST.get('sample_papers', 0))

            # Simple ML prediction using weighted formula
            # (In production, load a trained sklearn model using joblib)
            predicted_score = (
                study_hours * 3.5 +
                attendance * 0.3 +
                previous_score * 0.25 +
                sleep_hours * 1.5 +
                sample_papers * 2.0
            )
            # Clamp between 0 and 100
            predicted_score = max(0, min(100, round(predicted_score, 2)))

            grade = get_grade(predicted_score)
            color = get_performance_color(predicted_score)

            context = {
                'predicted_score': predicted_score,
                'grade': grade,
                'color': color,
                'study_hours': study_hours,
                'attendance': attendance,
                'previous_score': previous_score,
                'sleep_hours': sleep_hours,
                'sample_papers': sample_papers,
            }
            return render(request, 'predictor/result.html', context)

        except (ValueError, TypeError) as e:
            error_message = "Invalid input. Please enter valid numbers."
            return render(request, 'predictor/home.html', {'error': error_message})

    return render(request, 'predictor/home.html')
