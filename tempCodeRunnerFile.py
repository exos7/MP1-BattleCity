    if boundingBoxCollisionBullet(bullet, shield):
                                if bullet in enemy.bullets:
                                    enemy.bullets.remove(bullet)
                                if shield in self.player.shields:
                                    self.player.shields.remove(shield)
                                pyxel.play(0, 4)
                                print('shield was hit')