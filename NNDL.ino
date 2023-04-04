int bulb1 = A0; // Pin for bulb 1
int bulb2 = A1; // Pin for bulb 2

void setup() {
  // Set bulb pins as outputs
  pinMode(bulb1, OUTPUT);
  pinMode(bulb2, OUTPUT);

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // Wait for serial input
  while (Serial.available() == 0) {}

  // Read serial input
  char cmd = Serial.read();

  // Turn on/off bulbs based on serial input
  if (cmd == '1') {
    digitalWrite(bulb1, HIGH);
  } else if (cmd == '2') {
    digitalWrite(bulb1, LOW);
  } else if (cmd == '3') {
    digitalWrite(bulb2, HIGH);
  } else if (cmd == '4') {
    digitalWrite(bulb2, LOW);
  }
}
