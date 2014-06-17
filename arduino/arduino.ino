// digital pin 2 has a pushbutton attached to it. Give it a name:
int paddleButton = 2;
int stairButton = 3;
int paddleState = 0;
int stairState = 0;
int prevPaddleState = 0;
int prevStairState = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(paddleButton, INPUT);
  pinMode(stairButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  prevPaddleState = paddleState;
  paddleState = digitalRead(paddleButton);
  
  prevStairState = stairState;
  stairState = digitalRead(stairButton);
  
  if(paddleState == 1 && prevPaddleState == 0){
    Serial.print("t");
  }
  
  if(stairState == 1){
    Serial.print("f");
  } else if(stairState == 0) {
    Serial.print("g");
  }
  
  delay(10);        // delay in between reads for stability
}



