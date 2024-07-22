class Band:

    all = []

    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        Band.all.append(self)
        self.band_shows = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):
        if hometown == self.hometown and isinstance(hometown, str) and len(hometown) > 0:
            self._hometown = hometown

    def concerts(self):
        band_concerts = [concert for concert in Concert.all if concert.band == self] 
        return band_concerts if len(band_concerts) > 0 else None

    def venues(self):
        available_venues_list = []
        for concert in Band.concerts(self):
            if not(concert.venue in available_venues_list):
                available_venues_list.append(concert.venue)
        return available_venues_list if len(available_venues_list) > 0 else None

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        return new_concert

    def all_introductions(self):
        all_venues = Band.venues(self)
        intros_song_list = []
        if len(all_venues) == 0:
            return None
        else:
            for venue in all_venues:
                intros_song_list.append(f"Hello {venue.city}!!!!! We are {self.name} and we're from {self.hometown}")
        return intros_song_list

############################## CLASS WITH THE SSOT ##############################
class Concert:

    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

############################################################################

class Venue:

    all = []

    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list(set([concert.band for concert in Concert.all if concert.venue == self]))
    

