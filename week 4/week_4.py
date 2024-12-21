items=[
    {
    'id':i+100,
    'no_of_bids':0,
    'reserved_price':0,
    'description':'',
    'max_bid':0,
    'sold':False
    }
    for i in range(10)
    ]
bidders=[
    ]

def input():
    print('         input the data :\n\n')
    for j in range(10):
        print('    *** Item Id : ',items[j]['id'])
        items[j]['reserved_price']=int(input('reserve bid is : '))
        items[j]['description']=input('description : ')


def menu():
    print('           *** MENU ***')
    for k in range(10):
        if items[k]['sold']==False:
            print('\n\n       *** Record start ***')
            print('Item Id       : ',items[k]['id'])
            print('Reserve-Price : ',items[k]['reserved_price'])
            print('No.of Bids    : ',items[k]['no_of_bids'])
            print('Highest bid   : ',items[k]['max_bid'])
            print('Description   : ',items[k]['description'])
            print('       *** Record Ended ***')




