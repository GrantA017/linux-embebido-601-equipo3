#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

#define LED_DDR DDRB
#define LED_PORT PORTB

int main(){
    LED_DDR = 0b00111111;
    
    PORTB = 0xFF;
    while(1) {
        for (int i = 0; i < 6; i++){
            LED_PORT = (1 << i);
            _delay_ms(500);

            LED_PORT &= ~(1 << i);
            _delay_ms(500);
        }
    }
}