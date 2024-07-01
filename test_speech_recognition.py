try:
    import speech_recognition as sr
    print("speech_recognition module is successfully imported.")
except ModuleNotFoundError as e:
    print(f"Error: {e}")
