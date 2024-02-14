# from flask import Flask

# app = Flask(__name__)

# if app.config["ENV"] == "production":
#     app.config.from_object("config.DevelopmentConfig")
# elif app.config["ENV"] == "testing":
#     app.config.from_object("config.TestingConfig")
# else:
#     app.config.from_object("config.ProductionConfig")

# from app import views


from flask import Flask

app = Flask(__name__)

# Set the environment explicitly
app.config["ENV"] = "development"  # or "production", "testing"

if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
