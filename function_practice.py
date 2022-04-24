def hello():
    print (f'Hello')

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(item_list):
    if len(item_list) <= 0:
        print(f'My lunchbox is empty!')
    else:
        for index, item in enumerate( item_list):
            if index == 0:
                print( f'First I eat { item } ')
            else:   
                print(f'Next I eat  { item }')


hello()
list_item = pack('item11', 'item22', 'item33')
print(list_item)

eat_lunch(list_item)