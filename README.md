# spring-pendulum-investigation
Projects related to the investigation into unique behaviour in spring-pendulum systems

### 2023-04-27 (v0.1):
- Phase space of simple pendulum
	- Phase space represented as vector field using pyplot quiver
	- Normalised vector field
	- Implemented colour mapping to encode magnitude
	- Colorbar for cmap scale
- Computation of position of simple pendulum
	- Simple pendulum program used to test out ideas before implementing into main
	- Point mass of simple pendulum systems position computed over specified time
	- Computes position based on initial state vector:
		- theta
		- theta dot
	- with coefficient of air resistance factored in
- Computation of position of spring-pendulum
	- Point mass of spring-pendulum systems position computed over specified time
	- Computes postition based on an initial state vector:
		- theta 
		- theta dot
		- length
		- length dot
	- and the initial conditions:
		- spring constant
		- coefficient of air resistance
		- mass
		- rest length
- Implemented Animation of change of state vector
	- Animates state vector through time
	- Graphs the state vector through the systems phase flow
- Implemented Animation of motion of spring-pendulum
	- Files saved as Mp4
	- "real-time" playback
	- Parameters encoded in title
	- Initial conditions encoded in title

	
