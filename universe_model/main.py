from Box2D.examples.framework import Framework
from Box2D import *


class Simulation(Framework):
    def __init__(self):
        super(Simulation, self).__init__()

        # Default gravity disable
        self.world.gravity = (0.0, 0.0)
        # Gravity constant
        self.G = 100

        # Planet
        sun = b2FixtureDef(shape=b2CircleShape(radius=5), density=1, friction=0.5, restitution=0.5)
        self.world.CreateBody(type=b2_dynamicBody, position=b2Vec2(0,0), fixtures=sun)

        # Satellite
        circle_small = b2FixtureDef(shape=b2CircleShape(radius=0.2), density=1, friction=0.5, restitution=0.2)
        circle_medium = b2FixtureDef(shape=b2CircleShape(radius=0.3), density=1, friction=1.0, restitution=0.5)
        circle_big = b2FixtureDef(shape=b2CircleShape(radius=0.5), density=1, friction=1.0, restitution=0.6)
        self.world.CreateBody(type=b2_dynamicBody, position=b2Vec2(0, 6), fixtures=circle_small,
                              linearVelocity=(37, 0))
        self.world.CreateBody(type=b2_dynamicBody, position=b2Vec2(0, 10), fixtures=circle_small,
                              linearVelocity=(28, 0))
        self.world.CreateBody(type=b2_dynamicBody, position=b2Vec2(0, 15), fixtures=circle_medium,
                              linearVelocity=(22, 0))
        self.world.CreateBody(type=b2_dynamicBody, position=b2Vec2(0, 20), fixtures=circle_big,
                              linearVelocity=(16, 0))
    def Step(self, settings):
        super(Simulation, self).Step(settings)

        # Simulate the Newton's gravity
        for bi in self.world.bodies:
            for bk in self.world.bodies:
                if bi == bk:
                    continue

                pi, pk = bi.worldCenter, bk.worldCenter
                mi, mk = bi.mass, bk.mass
                delta = pk - pi
                r = delta.length
                if abs(r) < 1.0:
                    r = 1.0

                force = self.G * mi * mk / (r * r)
                delta.Normalize()
                bi.ApplyForce(force * delta, pi, True)


if __name__ == "__main__":
    Simulation().run()
