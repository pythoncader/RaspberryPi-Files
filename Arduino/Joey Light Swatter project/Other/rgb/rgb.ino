int red_light_pin= 3;
int green_light_pin = 5;
int blue_light_pin = 6;
int delay_value = 150;
void setup() {
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}
void loop() {
  RGB_color(255, 0, 0); // Red
  delay(delay_value);
  //RGB_color(0, 255, 0); // Green
  //delay(delay_value);
  RGB_color(0, 0, 255); // Blue
  delay(delay_value);
  //RGB_color(255, 255, 125); // Raspberry
  //delay(delay_value);
  //RGB_color(0, 255, 255); // Cyan
  //delay(delay_value);
  //RGB_color(255, 0, 255); // Magenta
  //delay(delay_value);
  //RGB_color(255, 255, 0); // Yellow
  //delay(delay_value);
  RGB_color(255, 255, 255); // White
  delay(delay_value);
}
void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}
