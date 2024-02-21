<h1>Beehive_Monitor - FinalProject</h1>

<h2>Summary</h2>
<p style="font-size:10px">HiveGuard is a prototype of a beehive monitor system. Its purpose is to observe bee traffic entering and exiting a hive. The project consists of two main parts: an app collecting sensor data, with a function of sending email notification when a potential swarming is detected and a web application visualising the data.</p>

<h2>Prerequisites</h2>
<h3>Hardware:</h3>
<ul>
  <li>Raspberry Pi</li>
  <li>IR sensors (at least two)</li>
  <li>Soldering kit</li>
  <li>Breadboard</li>
  <li>Jumper wires</li>
</ul>
<h3>Software:</h3>
<ul>
  <li>Python 3.11</li>
  <li>Node Package Manager</li>
</ul>

<h2>Setup</h2>

```
cd ../RaspberryPi/app
python3 bee_monitor_app.py
```

```
cd ../hiveguard
npm i
npm run dev
```

<h2>Project status</h2>
<p>In progress...</p>
