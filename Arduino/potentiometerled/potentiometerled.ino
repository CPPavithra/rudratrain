#define LED_PIN 11
#define P_PIN A0

void setup()
{
  pinMode(LED_PIN, OUTPUT);
}

void loop()
{
  int pValue = analogRead(P_PIN);
  int brightness = pValue;
  analogWrite(LED_PIN, brightness);
}
