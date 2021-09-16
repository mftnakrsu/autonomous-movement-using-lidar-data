# Lidar ile Otonom Hareket

Merhaba arkadaşlar, ROS simülasyon ortamında lidar ile otonom sürüşe giriş yapıyoruz. Gerekli kurulumlarlar aşağıda anlatılmıştır. 

## Gerekli Kurulumlar 

### sh kurulumu 

- Önecelikle ctrl + alt + t ile cmd açıp,   komutunu girelim.

      sudo apt-get update 

- Repoda paylaştığım kurulumlar.sh dosyayı nıçalıştırıp kurulumların hepsini tamamlayalım, yes/no dediği her bölümde yes diyerek onaylayalım.  

      sh kurulumlar.sh

- Terminalimizi açalım ve  <code>git clone  https://github.com/richardw05/mybot_ws</code> diyelim.

- Ardından aynı terminalde  <code>mybot_ws</code> dizinimize gidelim .  <code>catkin_make</code> diyelim ve home dizinimize geri dönelim.

- Daha sonra  <code>gedit ~/.bashrc</code> diyelim ve bashrc dosyamıza,  <code>source /home/kullanici_adiniz/mybot_ws/devel/setup.bash</code> satırını ekleyelim, kaydedip çıkalım.

- Son olarak terminale gelip:  <code>source ~/.bashrc</code> diyelim ve terminalimizi kapatalım.

### Turtlebot3 Kurulumu

    sudo apt-get install ros-melodic-turtlebot3-*  
    cd ~/catkin_ws/src/  
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git  
    git clone https://github.com/ROBOTIS-GIT/turtlebot3.git  
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations  
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_autorace  
    cd ~/catkin_ws && catkin_make  

Daha sonra,

    gedit ~/.bashrc

Açılan dosyada en alt satıra gelip export  <code>TURTLEBOT3_MODEL=waffle</code> ekliyoruz. Kaydedip dosyayı kapatalım. Daha sonra terminale gelip:  <code>source ~/.bashrc</code> diyelim ve terminalimizi kapatalım.

### Gazebo 

    gazebo  
![alt text](https://github.com/mftnakrsu/autonomous-movement-using-lidar-data/blob/main/imgs/1.png)  
veya  

    roslaunch mybot_gazebo mybot_world.launch  
![alt text](https://github.com/mftnakrsu/autonomous-movement-using-lidar-data/blob/main/imgs/2.png)  


Şimdi de hazır olan bir map'i launch edelim. 

    roslaunch mybot_gazebo mybot_world.launch  
![alt text](https://github.com/mftnakrsu/autonomous-movement-using-lidar-data/blob/main/imgs/4.png)  

### rViz  

    roslaunch mybot_description mybot_rviz.launch      
![alt text](https://github.com/mftnakrsu/autonomous-movement-using-lidar-data/blob/main/imgs/5.png)  

