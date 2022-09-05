var sink_id = "";

navigator.mediaDevices.enumerateDevices()
    .then(inspect_devices)
    .catch(errorCallback);

function inspect_devices(deviceInfos) {
  console.log("Inspecting Devices: " + deviceInfos.length + " device(s) total (audio/video input/output)");
  for (var deviceIdx = 0; deviceIdx < deviceInfos.length; deviceIdx++) {
    var deviceInfo = deviceInfos[deviceIdx];
    if ((deviceInfo.kind == "audiooutput") && (deviceInfo.label.includes("VB-Audio") || deviceInfo.label.includes("BlackHole"))) {
      sink_id = deviceInfo.deviceId;
      update_all_sinks();
    }
  }
}

function update_all_sinks() {
  var allMedia = document.querySelectorAll("audio,video");
  for (var mediaElement = 0; mediaElement < allMedia.length; mediaElement++) {
    allMedia[mediaElement].setSinkId(sink_id);
  }
}

function errorCallback(error) {
	console.log("Error: "+ error);
}