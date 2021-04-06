>> The traditional autonomy architecture of estimation, planning, and control is a:<<

( ) physical architecture
(x) logical architecture
( ) a resource graph
( ) a computation graph

[explanation]
The traditional control pipeline is a logical architecture. It informs which signals originate and end up where, but provides no information on actual implementation.
[explanation]

>> Physical architectures differ from logical ones because: <<

( ) They are more difficult to design and require endurance. 
( ) Physical architectures are not reproducible between instantiations of different hardware, while logical architectures are immutable.
(x) They detail implementation details such as which processors run which processes, and through which media signals flow. 

>>In computation graphs:<<

(x) nodes are software processes.
(x) edges are signals.
( ) nodes are procesors.
( ) edges are physical or wireless data links.

>>In resources graphs:<<

(x) the size of nodes represents computation power.
( ) the size of nodes represents computation needed.
( ) the thickness of edges represents the bandwidth needed for signals.
(x) the thickness of edges represents the available bandwidth.

>> What does the "bandwidth" of a communication channel inform us about?<<

( ) what kind of data can be transferred on a given link.
(x) how much data can be transferred in a unit of time on a given link.
( ) what software processes can be deployed on that channel.

>> What is a synonym of "latency"?<<

( ) Update frequency
(x) Time delay
( ) Power efficiency
( ) Performance penalty

>> Why is deployment difficult?<<

(x) Because code running various software processes must be broken down and ran on different processors, possibly on different computers, often implying duplication and overhead.
(x) Because there are many combinations of deployment to choose from.
(x) Because there is great variability in some factors such as network performances.
(x) Because no two pieces of hardware are ever the same.

[explanation]
Reliable, reproducible deployment is the difficult (and fun!) part of robotics. That's why it's important to learn using a real robot.
[explanation]
