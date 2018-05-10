# Home_Monitor
A simple House Monitor programe with a WebUI

# Install
`pip install -r requirments.txt`

`pip install gunicorn`

# Usage
INPUT YOUR CAM ID FIRST
## Main function
1. Monitor: Monitoring your house. You can choose local model or remote model.
2. Add your photo: Take a photo for you and your friends. You may need to create a floder named "image"
3. Del photo: Del your photo by name
4. Clear All alert history: Clear all alert image
6. Quit
## WEBUI
run `./start.sh`
It will listen on 0.0.0.0:8000
run `./stop.sh` to stop
# Thanks
https://www.jianshu.com/p/75fc00764d21
https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
https://www.cnblogs.com/arkenstone/p/7159615.html
