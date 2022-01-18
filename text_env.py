from dotenv import dotenv_values
import os

api = dotenv_values(".env")
print(api["KEY_API"])
