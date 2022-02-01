{
      'name': 'Travels Management',
      'depends': ['base'],
      'application': True,
      'data': [
          'data/sequence.xml',
          'data/tour_packages.xml',
          'data/location.xml',
          'data/facilities.xml',
          'security/ir.model.access.csv',
          'views/travels_management_booking_views.xml',
          'views/travels_management_service_types_views.xml',
          'views/travels_management_vehicle_views.xml',
          'views/travels_management_tour_package_views.xml',
          'views/travels_management_menus.xml',

           ]
}
