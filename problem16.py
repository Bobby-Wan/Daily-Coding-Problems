# This problem was asked by Twitter.
# You run an e-commerce website and 
# want to record the last N order ids 
# in a log. Implement a data structure 
# to accomplish this, with the 
# following API:
# record(order_id): adds the order_id 
# to the logget_last(i): gets the ith 
# last element from the log. i is 
# guaranteed to be smaller than or equal 
# to N. You should be as efficient with 
# time and space as possible.

#this program assumes that order ids 
#are stored in normal sized integers
import os
import sys
from array import array

log_file_name = 'order_log'
integer_size = sys.getsizeof(int)

#while working with logger, order ids are kept in memory. 
#the log() method saves ids to file.
#on object construction, the ids are loaded from the log file.
class Order_Logger:
    def __init__(self, max_orders):
        print('in constructor...')

        if os.path.isfile(log_file_name):
            f = open(log_file_name,'rb')
            data = f.read()
            print('binary data read: ', data)

            self.order_ids = array('I')
            self.order_ids.fromstring(data)
            print('loaded data: ', self.order_ids)

            self.max_ids = max(len(self.order_ids), max_orders)
            print('max orders: ', self.max_ids)
        else:
            f = open(log_file_name,'x')
            f.close()
            print('created logging file.')
            self.order_ids = array('I')
            self.max_ids = max_orders
    
    def log(self):
        if not os.path.isfile(log_file_name):
            f=open(log_file_name,'x')
            print('created log file.')
            f.close()

        print('ids to save: ', self.order_ids)
        f = open(log_file_name, 'wb')
        self.order_ids.tofile(f)
        f.close()

    def append_order(self, order_id):
        while len(self.order_ids) >= self.max_ids:
            print('removing last order: ', self.order_ids.pop(0))
            
        print('adding new order: ', order_id)
        self.order_ids.append(order_id)

    def get(self, index):
        print('in memory: ', self.order_ids)
        if index >= len(self.order_ids) or index < 0:
            return -1
        return self.order_ids[index]

def main():
    logger = Order_Logger(50)
    logger.append_order(11)
    logger.append_order(12)

    logger.log()

if __name__ == '__main__':
    main()
        
        

        