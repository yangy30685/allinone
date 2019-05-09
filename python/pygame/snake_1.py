from snake_2 import *

def main():
    score = 0
    
    #Snake initialization
    mySnake = Snake(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    mySnake.setDirection(KEY["UP"])
    mySnake.move()
    start_segments=3
    
    while(start_segments>0):
        mySnake.grow()
        mySnake.move() 
        start_segments-=1

    #Apples
    max_apples = 1
    eaten_apple = False
    apples = [Apple(random.randint(60,SCREEN_WIDTH),random.randint(60,SCREEN_HEIGHT),1)]
    respawnApples(apples,max_apples,mySnake.x,mySnake.y)
    
    startTime = pygame.time.get_ticks()
    endgame = 0
    
    while(endgame!=1):
        gameClock.tick(FPS)

        #Input
        keyPress = getKey()
        if keyPress == "exit":
            endgame = 1
       
        #Collision check
        checkLimits(mySnake)
        if(mySnake.checkCrash()== True):
            endGame()
            
        for myApple in apples:
            if(myApple.state == 1):
                if(checkCollision(mySnake.getHead(),SNAKE_SIZE,myApple,APPLE_SIZE)==True):
                    mySnake.grow()
                    myApple.state = 0
                    score+=5
                    eaten_apple=True

        #Position Update
        if(keyPress):
            mySnake.setDirection(keyPress)    
        mySnake.move()
        
        #Respawning apples
        if(eaten_apple == True):
            eaten_apple = False
            respawnApple(apples,0,mySnake.getHead().x,mySnake.getHead().y)

        #Drawing
        screen.fill(background_color)
        for myApple in apples:
            if(myApple.state == 1):
                myApple.draw(screen)
                
        mySnake.draw(screen)
        drawScore(score)
        gameTime = pygame.time.get_ticks() - startTime
        drawGameTime(gameTime)
        
        pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':     
    main()