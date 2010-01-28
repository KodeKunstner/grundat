# -*- coding: utf-8 -*-


class TransportMiddel(object):
    def __init__(self, ejer_navn, hastighed=0):
        """ Initialiser transportmidlet """
        self.tilstand  = "stoppet"
        self.hastighed = hastighed
        self.ejer_navn = ejer_navn


    def getTilstand(self):
        """ hent transportmidlets tilstand """
        return self.tilstand

    def setTilstand(self, tilstand):
        """ sæt transportmidlets tilstand """
        self.tilstand = tilstand


    def getEjerNavn(self):
        """ hent navnet på transportmidlets ejer """
        return self.ejer_navn

    def getHastighed(self):
        """ hent transportmidlets hastighed """
        return self.hastighed


    def start(self):
        """ start transportmidlet """
        self.setTilstand("startet")

    def stop(self):
        """ stop transportmidlet """
        self.setTilstand("stoppet")

    def forlad(self):
        """ forlad transportmidlet """
        if self.getTilstand() != "stoppet":
            print "ADVARSEL: Du er ved at forlade transportmidlet uden først at stoppe!"
        self.tilstand = "efterladt"


class Cykel(TransportMiddel):
    def start(self):
        """ start cyklen """
        TransportMiddel.start(self)
        print '%s sprinter afsted på sin cykel med %i km/t.' % (self.getEjerNavn(), self.getHastighed())

    def stop(self):
        """ stop cyklen """
        TransportMiddel.stop(self)
        print '%s bremser og stopper cyklen.' % (self.getEjerNavn())

    def forlad(self):
        """ stig af cyklen """
        TransportMiddel.forlad(self)
        print '%s stiger af cyklen.' % (self.getEjerNavn())


class Bil(TransportMiddel):
    def __init__(self, hastighed, ejer_navn, nummerplade):
        """ initialiser bilen """
        TransportMiddel.__init__(self, hastighed, ejer_navn)
        self.nummerplade = nummerplade

    def getNummerplade(self):
        """ hent bilens nummerplade """
        return self.nummerplade

    def start(self):
        """ start bilen """
        TransportMiddel.start(self)
        print "%s tøffer afsted i sin bil med %i km/t (nummerplade: %s)." % \
            (self.getEjerNavn(), self.getHastighed(), self.getNummerplade())

    def stop(self):
        """ stop bilen """
        TransportMiddel.stop(self)
        print '%s parkerer bilen.' % (self.getEjerNavn())

    def forlad(self):
        """ stig ud af bilen """
        TransportMiddel.forlad(self)
        print '%s åbner døren og går ud af bilen.' % (self.getEjerNavn())


class Fly(TransportMiddel):
    def __init__(self, ejer_navn, passager, hastighed=0):
        """ initialiser fly """
        TransportMiddel.__init__(self, ejer_navn, hastighed)
        self.passager = passager

    def getPassager(self):
        """ hent navnet på flyets passager """
        return self.passager

    def start(self):
        """ start flyet """
        TransportMiddel.start(self)
        print "%s farer afsted i %s's fly med %i km/t." % (self.getPassager(), self.getEjerNavn(), self.getHastighed())

    def stop(self):
        """ flyv ned i lavere højde """
        TransportMiddel.stop(self)
        print '%s sænker flyet til en passende højde.' % (self.getPassager())

    def forlad(self):
        """ forlad flyet """
        TransportMiddel.forlad(self)
        print '%s tager faldskærm på og hopper ud af flyet!' % (self.getPassager())


# Start og stop cykel
cykel = Cykel('Stefan', 23)
cykel.start()
cykel.stop()
cykel.forlad()
print ""

# Start og stop bil
bil = Bil('Karl', 130, nummerplade='AD 23 210')
bil.start()
bil.forlad()
print ""

# Start og stop fly
fly = Fly('SAS', 'Troels', 1000)
fly.start()
fly.stop()
fly.forlad()
