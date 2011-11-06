// Developed by Tatiana Al-Chueyr and Álvaro Justen
// License: GPLv2 http://www.gnu.org/licenses/gpl-2.0.html

#define SLAP 1
#define F1 2
#define F2 4
#define F3 8
#define F4 16
#define F5 32

#define F1_PIN 12
#define F2_PIN 11
#define F3_PIN 10
#define F4_PIN 9
#define F5_PIN 8
#define SLAP_PIN_UP 4
#define SLAP_PIN_DOWN 5

void setup() {
  Serial.begin(115200);
  pinMode(F1_PIN, INPUT);
  pinMode(F2_PIN, INPUT);
  pinMode(F3_PIN, INPUT);
  pinMode(F4_PIN, INPUT);
  pinMode(F5_PIN, INPUT);
  pinMode(SLAP_PIN_UP, INPUT);
  pinMode(SLAP_PIN_DOWN, INPUT);

  digitalWrite(F1_PIN, HIGH);
  digitalWrite(F2_PIN, HIGH);
  digitalWrite(F3_PIN, HIGH);
  digitalWrite(F4_PIN, HIGH);
  digitalWrite(F5_PIN, HIGH);
}

void loop() {
  char buttonsValues = 0;
  int slap_status = LOW;
  buttonsValues += F1 * digitalRead(F1_PIN);
  buttonsValues += F2 * digitalRead(F2_PIN);
  buttonsValues += F3 * digitalRead(F3_PIN);
  buttonsValues += F4 * digitalRead(F4_PIN);
  buttonsValues += F5 * digitalRead(F5_PIN);
  buttonsValues += SLAP * (digitalRead(SLAP_PIN_UP) && digitalRead(SLAP_PIN_DOWN));

  Serial.print(buttonsValues);  
}
