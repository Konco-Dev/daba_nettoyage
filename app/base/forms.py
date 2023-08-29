# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms import ValidationError
# from wtforms.validators import Email, DataRequired
#
# from app.base.models import Subscriber
#
#
# class SubscriptionForm(FlaskForm):
#
#     fullname =StringField("FullName", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#
#     def validate_email(self, field):
#         check_email = Subscriber.query.filter_by(email=field.data).first()
#         if check_email:
#             error = "Thank you for your interest, it seems that you have already subscribed to our newsletter, we'll notify you as soon as the website is up!"
#             raise ValidationError(error)
