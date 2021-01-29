//Varying_LED_Brightness

int lightval = 0;
int counter = 1;

void setup() {
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);       //Declare which variables are outputs.
  pinMode(11,OUTPUT);
}

void loop() {
  if(counter <= 0){         //Switch to add to counter.
    lightval = 1;
    }
  if(counter >= 45){       //Switch to subrtact from counter.
    lightval = 0;
    }
  if(lightval == 1){        //Start adding to the counter.
    ++counter;
    }
  if(lightval == 0){        //Start subtracting from the counter.
    --counter;
    }
  analogWrite(9,counter);   
  analogWrite(10,counter);  //Turn the LEDs on at the value of the counter.
  analogWrite(11,counter);
  delay(30);                //Wait 30 milliseconds.
}
