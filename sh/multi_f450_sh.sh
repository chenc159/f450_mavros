gnome-terminal --window -e 'bash -c "roslaunch f450 f450_test.launch uavID:=uav1 tgt_system:=1; exec bash"' \
--tab -e 'bash -c "sleep 2; roslaunch f450 f450_test.launch uavID:=uav2 tgt_system:=2; exec bash"' \
--tab -e 'bash -c "sleep 2; rosrun outdoor_gcs outdoor_gcs; exec bash"' \