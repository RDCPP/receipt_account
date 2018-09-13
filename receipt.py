from operator import itemgetter, attrgetter

class Receipt:
    def __init__(self,description,price):
        self.description = description
        self.price = price

    def print_data(self):
        print("Receipt Description : " + self.description + "\n" + "Receipt Price       : " + str(self.price))

    # def __lt__(self,other):
    #     return self.price < other.price

def main():

    border_price = int(input("What is the minimum price? : "))
    receipt_data = []
    total_price = input_data(receipt_data)
    receipt_data = sorted(receipt_data, key=lambda receipt: receipt.price ,reverse=True)
    if(total_price > border_price):
        total_receipt = compute_receipt(total_price,border_price,receipt_data)
    
def input_data(receipt_data):

    total_price = 0

    while(True):

        description = input("Please write your receipt description. \n(If you do not have any receipts left, please enter quit) : ")        
        if(description == "quit"): break       
        price = int(input("Please write your receipt price. : "))
        total_price += price
        receipt = Receipt(description,price)
        receipt_data.append(receipt)
        receipt_data[len(receipt_data) - 1].print_data()

    return total_price

def compute_receipt(total_price,border_price,receipt_data):

    i = 0 # 리스트 참조 변수
    use_price = 0 # 계산 후 돌려줄 일정 값 이상의 최솟값
    use_list = [] # 계산 후 돌려줄 일정 값들의 리스트 모임
    second_receipt_data = [] # 영수증 데이터에서 반드시 들어가야 될 값을 제한 나머지 리스트

    while(True):

        if(total_price - receipt_data[i].price < border_price):
        # 제 1 경우 : 얘가 없으면 안됨
            use_price += receipt_data[i].price
            use_list.append(receipt_data[i])
            i += 1

        elif(total_price - receipt_data[i].price == border_price):
        # 제 2 경우 : 얘만 없으면 딱 맞음
            use_price = border_price
            use_list = receipt_data[:i] + receipt_data[i+1:]
            return [use_price,use_list]

        else:
        # 제 3 경우 : 얘는 있어도 되고 없어도 됨
            second_receipt_data = receipt_data[i:]
            break

    second_border = border_price - use_price # 최소컷을 넘는 값 중에 필수값을 제한 나머지 값을 두번째 최소컷으로 잡음
    second_lower_border_list = [] # 2차 최소컷을 못 넘는 값들을 과정마다 저장함
    least_upper_second_border = total_price # 2차 최소컷 넘는 값 중에 최소값
    least_upper_second_border_list = [] # 2차 최소컷 넘는 값 중에 최소값들 리스트

    while(True): # 배열 중 2개를 더함

        for x in range(len(second_receipt_data)):
            for y in range(x+1,len(second_receipt_data)):

                tmp = second_receipt_data[x] + second_receipt_data[y]

                if(tmp > second_border and least_upper_second_border > tmp):
                    least_upper_second_border = tmp
                    least_upper_second_border_list = [second_receipt_data[x],second_receipt_data[y]]

                else:
                    pass


            
            
    return [use_price,use_list]

    


if __name__ == "__main__":
	main()