<h2>Users</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>GET</td><td>/users</td><td>index</td><td>List all users</td></tr>
  <tr><td>POST</td><td>/users</td><td>create</td><td>Create a new user</td></tr>
  <tr><td>GET</td><td>/users/:id</td><td>show</td><td>Show details of a user</td></tr>
  <tr><td>PUT/PATCH</td><td>/users/:id</td><td>update</td><td>Update user information or points</td></tr>
  <tr><td>DELETE</td><td>/users/:id</td><td>destroy</td><td>Delete a user</td></tr>
</table>

<h2>Cars</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>GET</td><td>/cars</td><td>index</td><td>List all cars</td></tr>
  <tr><td>POST</td><td>/cars</td><td>create</td><td>Create a new car</td></tr>
  <tr><td>GET</td><td>/cars/:id</td><td>show</td><td>Show details of a car</td></tr>
  <tr><td>PUT/PATCH</td><td>/cars/:id</td><td>update</td><td>Update a car</td></tr>
  <tr><td>DELETE</td><td>/cars/:id</td><td>destroy</td><td>Delete a car</td></tr>
</table>



<h2>User's Cars</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>POST</td><td>/users/:user_id/cars</td><td>create</td><td>Create a new car for a specific user</td></tr>
  <tr><td>GET</td><td>/users/:user_id/cars</td><td>index</td><td>List all cars belonging to a specific user</td></tr>
</table>




<h2>Parklots</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>GET</td><td>/parklots</td><td>index</td><td>List all parklots</td></tr>
  <tr><td>POST</td><td>/parklots</td><td>create</td><td>Create a new parklot</td></tr>
  <tr><td>GET</td><td>/parklots/:id</td><td>show</td><td>Show details of a parklot</td></tr>
  <tr><td>PUT/PATCH</td><td>/parklots/:id</td><td>update</td><td>Update a parklot</td></tr>
</table>



<h2>Parking Spots</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>GET</td><td>/parkingspots</td><td>index</td><td>List all parking spots</td></tr>
  <tr><td>POST</td><td>/parkingspots</td><td>create</td><td>Create a new parking spot</td></tr>
  <tr><td>PUT/PATCH</td><td>/parkingspots/:id</td><td>update</td><td>Update a parking spot</td></tr>
</table>



<h2>Parking Spots in a Parklot</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>GET</td><td>/parklots/:parklot_id/parkingspots</td><td>index</td><td>List all parking spots in a specific parklot</td></tr>
  <tr><td>POST</td><td>/parklots/:parklot_id/parkingspots</td><td>create</td><td>Create a new parking spot within a specific parklot</td></tr>
</table>


<h2>Reservations</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>GET</td><td>/reservations</td><td>index</td><td>List all reservations</td></tr>
  <tr><td>POST</td><td>/reservations</td><td>create</td><td>Create a new reservation</td></tr>
  <tr><td>GET</td><td>/reservations/:id</td><td>show</td><td>Show details of a reservation</td></tr>
  <tr><td>PUT/PATCH</td><td>/reservations/:id</td><td>update</td><td>Update a reservation</td></tr>
  <tr><td>DELETE</td><td>/reservations/:id</td><td>destroy</td><td>Delete a reservation</td></tr>
</table>




<h2>Reservations Related to User, Car, and Parking Spot</h2>
<table border="1">
  <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
  <tr><td>POST</td><td>/users/:user_id/cars/:car_id/parkingspots/:parkingspot_id/reservations</td><td>create</td><td>Create a reservation linking a user, car, and parking spot</td></tr>
</table>
