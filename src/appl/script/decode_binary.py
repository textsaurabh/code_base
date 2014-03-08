#! /usr/local/bin/python -u
"""
Script to decode binary.

Source: TopCoder SRM 144 DEV1, 300 Point Problem

"""
import operator
class BinaryCode(object):
    def __init__(self):
        pass

    def decode(self, message):
        """
        Decode the encoded message passed by the user.

        """
        assert(type(message) is str)
        ret_val = [None, None]

        # Assuming that the decoded message starts with 0
        decoded_msg_arr = ['0' for idx in range(len(message))]

        for idx, val in enumerate(message):
            val = int(val)
            # If we are at the first idx, then assume left side value is 0
            if idx == len(message) - 1:
                # Confirm that the last decoded number satisfies the equation
                if int(decoded_msg_arr[idx]) + int(decoded_msg_arr[idx-1]) == val:
                    break
                else:
                    decoded_msg_arr = None
                    break
            elif idx == 0:
                decoded_msg_arr[idx+1] = str(val - int(decoded_msg_arr[idx]) - 0)
                if int(decoded_msg_arr[idx+1] not in ('1', '0')):
                    decoded_msg_arr = None
                    break
            else:
                decoded_msg_arr[idx+1] = str(val - int(decoded_msg_arr[idx]) - int(decoded_msg_arr[idx-1]))
                if int(decoded_msg_arr[idx+1] not in ('1', '0')):
                    decoded_msg_arr = None
                    break

        ret_val[0] = "NONE" if decoded_msg_arr is None else reduce(operator.add, decoded_msg_arr)

        decoded_msg_arr = ['1' for idx in range(len(message))]

        for idx, val in enumerate(message):
            val = int(val)
            # If we are at the first idx, then assume left side value is 0
            if idx == len(message) - 1:
                # Confirm that the last decoded number satisfies the equation
                if int(decoded_msg_arr[idx]) + int(decoded_msg_arr[idx-1]) == val:
                    break
                else:
                    decoded_msg_arr = None
                    break
            elif idx == 0:
                decoded_msg_arr[idx+1] = str(val - int(decoded_msg_arr[idx]) - 0)
                if int(decoded_msg_arr[idx+1] not in ('1', '0')):
                    decoded_msg_arr = None
                    break
            else:
                decoded_msg_arr[idx+1] = str(val - int(decoded_msg_arr[idx]) - int(decoded_msg_arr[idx-1]))
                if int(decoded_msg_arr[idx+1] not in ('1', '0')):
                    decoded_msg_arr = None
                    break

        ret_val[1] = "NONE" if decoded_msg_arr is None else reduce(operator.add, decoded_msg_arr)

        print ret_val
        return tuple(ret_val)

def main():
    obj = BinaryCode()
    obj.decode("3")

if __name__ == '__main__':
    main()
