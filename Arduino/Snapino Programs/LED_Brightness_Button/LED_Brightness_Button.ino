//LED_Brightness_Button

int LEDstate = 0;
int buttonval = 0;
int oldbuttonval = 0;
int level = 0;
int brightness [] = {1, 2, 4, 8, 16, 32, 64, 128, 255, 0};  
                                        //Set up aray with LED brightness values
void setup() {
  pinMode(9,INPUT);
  pinMode(10,OUTPUT);
}

void loop() {
  buttonval = digitalRead(9);
  if((buttonval == LOW) && (oldbuttonval == HIGH)){
    LEDstate ++;
  }
  oldbuttonval = buttonval;
  if(LEDstate >= 1){
    LEDstate = 0;
    analogWrite(10,brightness[level]);  //Set LED brightness
    level ++;                           //Increment array to next value
    if (level >= 10) {                  //Reset array after last value is used
      level = 0; 
    }
    }
    delay(10);
}

