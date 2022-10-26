

let x = 0.01;
let y = 0
let z = 0;

let a = 10;
let b = 28;
let c = 8.0/3.0;



console.log(v);
function setup() {
  createCanvas(400, 400, WEBGL);
  background(0);
  
}

function draw() {

  let dt = 0.01;
  let dx = (a * (y - x)) * dt;
  let dy = (x * (b - z) - y) * dt;
  let dz = (x * y - c * z) * dt;
  x = x + dx;
  y = y + dy;
  z = z + dz;

 

 
  scale(5);
  stroke(255);


  point(x,y,z);

}
