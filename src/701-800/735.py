# 735. Asteroid Collision 
def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    s = []
    for a in asteroids:
        if len(s) == 0:
            s.append(a)
            
        # no collision (same direction)
        elif s[-1] * a > 0 or (s[-1] < 0 and a > 0):
            s.append(a)
        
        # collision (a is always negative and s is positive)
        else:
            # larger asteroid colliding with all smaller asteroids
            while (len(s) > 0) and (s[-1] > 0 and abs(a) > abs(s[-1])):
                s.pop()
            if len(s) == 0:
                s.append(a)
            # asteroids are equal and opposite directions
            elif s[-1] > 0 and abs(a) == abs(s[-1]):
                s.pop()
            # last asteroid is going in same direction
            elif s[-1] < 0:
                s.append(a)
                    
    return s