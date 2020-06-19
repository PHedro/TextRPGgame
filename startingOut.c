//
// Created by Frederico on 17/06/2020.
//

#include "startingOut.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int mainG(){
mainMenu();
    return 0;
}

SKILLS skills[10];
CHAR mChar;

/// MAIN MENU
void mainMenu(){
    char f = '1';
    while(1){
        printf("#### -- Welcome to NoNameGame -- ####\n(a)New Game\t(b)Load Game\n(c)Options\t(d)Terminate Game\n");
        char c[2];
        scanf("%s", c);
        f = c[0];
        switch(f){
            case '\n' : printf("Error in f char [breakline]\n"); return;
            case 'a': newGame(mChar); break;
            case 'b': break;
            case 'c': break;
            case 'd': return;
            default: printf("Hmm not quite right...\n");
        }
        f = '1';
    }
}
/// New Game
/// supposedly gets your name, if there already is a character with that name, it stops you, else it gets your info to create a new one
/// \param p1
void newGame(CHAR p1){
    int h = 0;
    print("Hmm, I see... you're new around here aren't you?\nIt's okay, you'll get the hang of it.\nWell, so... what's your name?\n");
    char answer[10]; getc(stdin);
    fgets(answer, 10, stdin);
//    if (!checkIfPlayerExists(name)) {
        strcpy(mChar.name, answer);
        mChar.lvl = 1;
        mChar.hp = 5;
        for(int i = 0; i < 10; i++){
            mChar.inv[i] = 0;
            mChar.skillT[i] = 0;
//        }

    }
        print("Hello"); printf( " %s!", mChar.name);print("It seems you're not here by chance alone as everyone else,\nthat's odd...\nBut ok, let's get you started:\n Do you identify as a common gender?\n");
    getc(stdin); fgets(answer, 10, stdin);
    _strlwr_s(answer, 10);
    /*switch(answer){
        case "yes": printf("%s - yes", answer); break;
        case "no": printf("%s - no", answer); break;
        case "male":
        case "boy":
        case "man":
        case "men": printf("%s - man", answer); break;
        case "female":
        case "woman" :
        case "girl": printf("%s - gril", answer); break;
    }*/
    if(strcmp(answer,"yes") == 0){
        print("Umm, duh, the real question was: what is it, moron?\n");
        getc(stdin); fgets(answer, 10, stdin);
        if(strcmp(answer, "male") == 0 || strcmp(answer, "man") == 0 || strcmp(answer, "boy") == 0){
            print("Oh yeah?\nTHEN FUCK DAMN CHAUVINIST\nWell umm anyway, do you have any experience with RPGs?\n");
            getc(stdin); fgets(answer, 10, stdin);

        }
    }
    else if(strcmp(answer,"no") == 0){
        print("Okay, then let's-----------\n Wait, what? What do you mean no?\n...\n...\nYou're weird\nAnyway. Do you have any experience with RPGs?\n");
        getc(stdin); fgets(answer, 10, stdin);
        if(strcmp(answer, "yes") == 0){
            print("Hmm ok. But how much?\n");
            getc(stdin); fgets(answer, 10, stdin);
            if(strcmp(answer, "lot") == 0 || strcmp(answer, "lots")){
                print("Okay, okay, smartass, you'll regret that, but okay.\n");
                mChar.dif = 3;
            }
            else if(strcmp(answer, "little") == 0 || strcmp(answer, "some") == 0){
                print("Really?\n...\nJust medium difficulty?\nHow original...\n");
                mChar.dif = 2;
            }
            else{

            }
        }
        else if(strcmp(answer, "no") == 0 || strcmp(answer, "nope") == 0 || strcmp(answer, "none") == 0){
            print("YES, finally some fresh meat. LET'S GET YOU STARTED\n");
            mChar.dif = 1;
        }
    }
    else if(strcmp(answer,"no") == 0){

    }
}
/// Simple function similar to printf, except that it writes more slowly, to get a little aesthetic
void print(char string[]){
    for(int a=0;string[a] != '\0';a++){
        printf("%c",string[a]);
        for(int t=0;t<=60000000;t++){
            int f = 0;
            f++;
        }
    }
}
///Dice roller, wich returns a value between 1 and 20, just like a real RPG
int roll20() {
    int n;
    do {
        n = rand() % 8;
    } while (n == 0 || n > 20);
    return n;
}
int checkIfPlayerExists(char *n); //TODO