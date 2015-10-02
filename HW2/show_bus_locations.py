import json
import sys
import urllib2

if __name__ == '__main__':
    url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (
        sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    mtadata = json.load(request)

    VehicleActivity = mtadata['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']
    num_bus = len(VehicleActivity)
    print 'Bus Line : %s' % sys.argv[2]
    print 'Number of Active Buses : %s' % num_bus
    for i in range(0, num_bus):
        Lat = VehicleActivity[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Latitude']
        Lon = VehicleActivity[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Longitude']    
        print 'Bus %s is at latitude %s and longitude %s' % (i, Lat, Lon)
