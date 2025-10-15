// METR4810 - Team 1 Garbage Truck - Motion Subsystem (L293D Version)

// --- Motor Pins ---
// Left Motor (Motor A)
const int LEFT_IN1 = 2;   // L293D pin 14
const int LEFT_IN2 = 3;   // L293D pin 10
const int ENABLE_L = 4;   // L293D pin 1 (enable motor A)

// Right Motor (Motor B)
const int RIGHT_IN1 = 8;  // L293D pin 7
const int RIGHT_IN2 = 9;  // L293D pin 2
const int ENABLE_R = 10;  // L293D pin 9 (enable motor B)

void setup() {
  // Initialize motor control pins as outputs
  pinMode(LEFT_IN1, OUTPUT);
  pinMode(LEFT_IN2, OUTPUT);
  pinMode(ENABLE_L, OUTPUT);

  pinMode(RIGHT_IN1, OUTPUT);
  pinMode(RIGHT_IN2, OUTPUT);
  pinMode(ENABLE_R, OUTPUT);

  // Enable motors at full speed (255 = max PWM)
  analogWrite(ENABLE_L, 255);
  analogWrite(ENABLE_R, 255);

  // Optional: start Serial monitor for debugging
  Serial.begin(9600);
}

// --- Motion Functions ---

// Move forward for a specified duration (in milliseconds)
void fwd() {
  Serial.println("Moving forward");
  digitalWrite(LEFT_IN1, LOW);
  digitalWrite(LEFT_IN2, HIGH);

  digitalWrite(RIGHT_IN1, HIGH);
  digitalWrite(RIGHT_IN2, LOW);
}

// Move backward for a specified duration (in milliseconds)
void bwd() {
  Serial.println("Moving backward");
  digitalWrite(LEFT_IN1, HIGH);
  digitalWrite(LEFT_IN2, LOW);

  digitalWrite(RIGHT_IN1, LOW);
  digitalWrite(RIGHT_IN2, HIGH);
}

// Turn in place (negative = right, positive = left)
void turn(int degree) {
  if (degree == 0) return;

  // Estimate turn duration — adjust this for your robot
  int turnTime = 1000;  // 1500 for hairpins

  if (degree < 0) {
    Serial.println("Turning left");
    // Left motor forward, right motor backward
    digitalWrite(LEFT_IN1, HIGH);
    digitalWrite(LEFT_IN2, LOW);

    digitalWrite(RIGHT_IN1, HIGH);
    digitalWrite(RIGHT_IN2, LOW);
  } else {
    Serial.println("Turning right");
    // Left motor backward, right motor forward
    digitalWrite(LEFT_IN1, LOW);
    digitalWrite(LEFT_IN2, HIGH);

    digitalWrite(RIGHT_IN1, LOW);
    digitalWrite(RIGHT_IN2, HIGH);
  }
  delay(turnTime);
}

// Stop all motors
void stop() {
  Serial.println("Stopping");
  digitalWrite(LEFT_IN1, LOW);
  digitalWrite(LEFT_IN2, LOW);

  digitalWrite(RIGHT_IN1, LOW);
  digitalWrite(RIGHT_IN2, LOW);
}

void straight() {
  fwd();
  delay(5500);
}

void hairpin(String dir) {
  if (dir == "right") {
    fwd();
    delay(2000);
    stop();
    turn(-90);
    fwd();
    delay(1000);
  } else {
      fwd();
      delay(2000);
      stop();
      turn(90);
      fwd();
      delay(1000);
    }
}

void curve(String dir) {
  if (dir == "left") {
    fwd();
    delay(2000);
    stop();
    turn(75);
    fwd();
    delay(500);
  } else {
      fwd();
      delay(2000);
      stop();
      turn(-75);
      fwd();   
    }
}

void crossroad(String dir) {
  fwd();
  delay(2000);
  if (dir == "fwd") {
    fwd();
    delay(1000);
  } else if (dir == "left") {
    turn(45);
    fwd();
    delay(1500);
  } else if (dir == "right") {
    turn(-45);
    fwd();
    delay(1500);
  } else {
    fwd();
    delay(5000);
  }  
}

void delivery_point() {
  fwd();
  delay(1500);
}

void loop() {
  //straight(); // For straight and chicane
  stop();
  while (1) {

  }
}
