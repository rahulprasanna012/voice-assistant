import speedtest
from Base.Mouth import speak

def get_internet_speed():
    try:
        speak("Checking your Internet speed. Please wait...")
        st = speedtest.Speedtest()

        # Get download and upload speed in Mbps
        download_speed = st.download() / 1_000_000  # Convert from bits to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert from bits to Mbps

        # Get ping (latency) in ms
        ping = st.results.ping

        # Report the speeds
        speak(f"Your download speed is {download_speed:.2f} Mbps.")
        speak(f"Your upload speed is {upload_speed:.2f} Mbps.")
        speak(f"Your ping is {ping:.2f} milliseconds.")

        # Return values for potential use elsewhere
        return {
            'download': download_speed,
            'upload': upload_speed,
            'ping': ping
        }
    except Exception as e:
        speak(f"An error occurred while checking internet speed: {str(e)}")
        return None

