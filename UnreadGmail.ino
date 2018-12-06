int LED = 13;
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {
  int response = Serial.read();
  if(response == '0')
  {
    digitalWrite(LED, LOW);
  }
  else if(response == '1'){
    digitalWrite(LED, HIGH);
  }

}
