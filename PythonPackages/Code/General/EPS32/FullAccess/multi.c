%
% multi.c
%
% ESP32 - Full Access
%
%


#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "sdkconfig.h"
  
#define BLINK_GPIO CONFIG_BLINK_GPIO
  
void blink_task(void *pvParameter) 
{
   gpio_pad_select_gpio(BLINK_GPIO);
   gpio_set_direction(BLINK_GPIO, GPIO_MODE_OUTPUT);
 
   while(1) {
     gpio_set_level(BLINK_GPIO, 0);
     vTaskDelay(1000 / portTICK_PERIOD_MS);
 
     gpio_set_level(BLINK_GPIO, 1);
     vTaskDelay(1000 / portTICK_PERIOD_MS);
   }
}
 
void hello_task(void *pvParameter) 
{
   while (1) 
   {
     printf("Hallo, Make-Magazin!\n");
     vTaskDelay(100 / portTICK_PERIOD_MS);
   }
}
 
void app_main() 
{
   xTaskCreate(&blink_task, "blink_task", 
   configMINIMAL_STACK_SIZE, NULL, 5, NULL);
   xTaskCreate(&hello_task, "hello_task",  
   configMINIMAL_STACK_SIZE, NULL, 5, NULL);
}

