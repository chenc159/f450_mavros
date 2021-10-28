
<!-- UAV1 -->
    <group ns="uav1">
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="1"/>
        <arg name="fcu_url" default="udp://:14541@localhost:14581"/>
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="0"/> <!-- 3,3 -->
            <arg name="y" value="0"/>
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14561"/>
            <arg name="mavlink_tcp_port" value="4561"/>
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>
    <!-- UAV2 -->
    <group ns="uav2">
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="2"/>
        <arg name="fcu_url" default="udp://:14542@localhost:14582"/>
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="1.0"/>
            <arg name="y" value="1.5"/>
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14562"/>
            <arg name="mavlink_tcp_port" value="4562"/>
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>
   
    <!-- UAV3 -->
    <group ns="uav3">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="3"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14543@localhost:14583"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="-3"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="-3"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14563"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4563"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>

    <!-- UAV4 -->
    <group ns="uav4">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="4"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14544@localhost:14584"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="3"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="-3"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14564"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4564"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>

    <!-- UAV5 -->
    <group ns="uav5">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="5"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14545@localhost:14585"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14565"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4565"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>

    <!-- UAV6 -->
    <group ns="uav6">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="6"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14546@localhost:14586"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14566"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4566"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>

    <!-- UAV7 -->
    <group ns="uav7">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="7"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14547@localhost:14587"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14567"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4567"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>

        <!-- UAV5 -->
    <group ns="uav8">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="8"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14548@localhost:14588"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14568"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4568"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>

    <!-- UAV9 -->
    <group ns="uav9">                                                   <!-- CHANGE THIS -->
        <!-- MAVROS and vehicle configs -->
        <arg name="ID" value="9"/>                                      <!-- CHANGE THIS -->
        <arg name="fcu_url" default="udp://:14549@localhost:14589"/>    <!-- CHANGE THIS -->
        <!-- PX4 SITL and vehicle spawn -->
        <include file="$(find px4)/launch/single_vehicle_spawn.launch">
            <arg name="x" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="y" value="0"/>                                   <!-- CHANGE THIS -->
            <arg name="z" value="0"/>
            <arg name="R" value="0"/>
            <arg name="P" value="0"/>
            <arg name="Y" value="0"/>
            <arg name="vehicle" value="$(arg vehicle)"/>
            <arg name="mavlink_udp_port" value="14569"/>                <!-- CHANGE THIS -->
            <arg name="mavlink_tcp_port" value="4569"/>                 <!-- CHANGE THIS -->
            <arg name="ID" value="$(arg ID)"/>
        </include>
        <!-- MAVROS -->
        <include file="$(find mavros)/launch/px4.launch">
            <arg name="fcu_url" value="$(arg fcu_url)"/>
            <arg name="gcs_url" value=""/>
            <arg name="tgt_system" value="$(eval 1 + arg('ID'))"/>
            <arg name="tgt_component" value="1"/>
        </include>
    </group>
    
