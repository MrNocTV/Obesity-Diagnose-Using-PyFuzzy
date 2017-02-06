import numpy as np
import skfuzzy as fuzz
import skfuzzy.control

from skfuzzy import *
class FuzzySystem:

    def __init__(self, bmi_start=0, bmi_stop=10, bf_start=0, bf_stop=10, wc_start=0, wc_stop=10, o_start=0, o_stop=10):
        """
        bmi : body mass index (kg / m^2)
        bf : body fat (%)
        wc : waist circumference (cm)
        o : obesity level
        """
        self.__bmi_start = bmi_start
        self.__bmi_stop = bmi_stop
        self.__bf_start = bf_start
        self.__bf_stop = bf_stop
        self.__wc_start = wc_start
        self.__wc_stop = wc_stop
        self.__o_start = o_start
        self.__o_stop = o_stop


    # these lines of code are pretty boring
    def set_bmi_low_start(self, start):
        self.__bmi_low_start = start

    def set_bmi_low_mid(self, mid):
        self.__bmi_low_mid = mid

    def set_bmi_low_stop(self, stop):
        self.__bmi_low_stop = stop

    def set_bmi_mod_start(self, start):
        self.__bmi_mod_start = start

    def set_bmi_mod_mid(self, mid):
        self.__bmi_mod_mid = mid

    def set_bmi_mod_stop(self, stop):
        self.__bmi_mod_stop = stop

    def set_bmi_high_start(self, start):
        self.__bmi_high_start = start

    def set_bmi_high_mid(self, mid):
        self.__bmi_high_mid = mid

    def set_bmi_high_stop(self, stop):
        self.__bmi_high_stop = stop

    def set_bmi_low(self, start, mid, stop):
        self.set_bmi_low_start(start)
        self.set_bmi_low_mid(mid)
        self.set_bmi_low_stop(stop)

    def set_bmi_mod(self, start, mid, stop):
        self.set_bmi_mod_start(start)
        self.set_bmi_mod_mid(mid)
        self.set_bmi_mod_stop(stop)

    def set_bmi_high(self, start, mid, stop):
        self.set_bmi_high_start(start)
        self.set_bmi_high_mid(mid)
        self.set_bmi_high_stop(stop)

    def set_bmi(self, low_start, low_mid, low_stop, mod_start, mod_mid, mod_stop, high_start, high_mid, high_stop):
        self.set_bmi_low(low_start, low_mid, low_stop)
        self.set_bmi_mod(mod_start, mod_mid, mod_stop)
        self.set_bmi_high(high_start, high_mid, high_stop)

    def set_bf_low_start(self, start):
        self.__bf_low_start = start

    def set_bf_low_mid(self, mid):
        self.__bf_low_mid = mid

    def set_bf_low_stop(self, stop):
        self.__bf_low_stop = stop

    def set_bf_nor_start(self, start):
        self.__bf_nor_start = start

    def set_bf_nor_mid(self, mid):
        self.__bf_nor_mid = mid

    def set_bf_nor_stop(self, stop):
        self.__bf_nor_stop = stop

    def set_bf_high_start(self, start):
        self.__bf_high_start = start

    def set_bf_high_mid(self, mid):
        self.__bf_high_mid = mid

    def set_bf_high_stop(self, stop):
        self.__bf_high_stop = stop

    def set_bf_low(self, start, mid, stop):
        self.set_bf_low_start(start)
        self.set_bf_low_mid(mid)
        self.set_bf_low_stop(stop)

    def set_bf_nor(self, start, mid, stop):
        self.set_bf_nor_start(start)
        self.set_bf_nor_mid(mid)
        self.set_bf_nor_stop(stop)

    def set_bf_high(self, start, mid, stop):
        self.set_bf_high_start(start)
        self.set_bf_high_mid(mid)
        self.set_bf_high_stop(stop)

    def set_bf(self, low_start, low_mid, low_stop, mod_start, mod_mid, mod_stop, high_start, high_mid, high_stop):
        self.set_bf_low(low_start, low_mid, low_stop)
        self.set_bf_nor(mod_start, mod_mid, mod_stop)
        self.set_bf_high(high_start, high_mid, high_stop)

    def set_wc_small_start(self, start):
        self.__wc_small_start = start

    def set_wc_small_mid(self, mid):
        self.__wc_small_mid = mid

    def set_wc_small_stop(self, stop):
        self.__wc_small_stop = stop

    def set_wc_med_start(self, start):
        self.__wc_med_start = start

    def set_wc_med_mid(self, mid):
        self.__wc_med_mid = mid

    def set_wc_med_stop(self, stop):
        self.__wc_med_stop = stop

    def set_wc_large_start(self, start):
        self.__wc_large_start = start

    def set_wc_large_mid(self, mid):
        self.__wc_large_mid = mid

    def set_wc_large_stop(self, stop):
        self.__wc_large_stop = stop

    def set_wc_small(self, start, mid, stop):
        self.set_wc_small_start(start)
        self.set_wc_small_mid(mid)
        self.set_wc_small_stop(stop)

    def set_wc_med(self, start, mid, stop):
        self.set_wc_med_start(start)
        self.set_wc_med_mid(mid)
        self.set_wc_med_stop(stop)

    def set_wc_large(self, start, mid, stop):
        self.set_wc_large_start(start)
        self.set_wc_large_mid(mid)
        self.set_wc_large_stop(stop)

    def set_wc(self, small_start, small_mid, small_stop, med_start, med_mid, med_stop, large_start, large_mid, large_stop):
        self.set_wc_small(small_start, small_mid, small_stop)
        self.set_wc_med(med_start, med_mid, med_stop)
        self.set_wc_large(large_start, large_mid, large_stop)

    def set_o_healthy_start(self, start):
        self.__o_healthy_start = start

    def set_o_healthy_mid(self, mid):
        self.__o_healthy_mid = mid

    def set_o_healthy_stop(self, stop):
        self.__o_healthy_stop = stop

    def set_o_over_start(self, start):
        self.__o_over_start = start

    def set_o_over_mid(self, mid):
        self.__o_over_mid = mid

    def set_o_over_stop(self, stop):
        self.__o_over_stop = stop

    def set_o_obese_start(self, start):
        self.__o_obese_start = start

    def set_o_obese_mid(self, mid):
        self.__o_obese_mid = mid

    def set_o_obese_stop(self, stop):
        self.__o_obese_stop = stop

    def set_o_healthy(self, start, mid , stop):
        self.set_o_healthy_start(start)
        self.set_o_healthy_mid(mid)
        self.set_o_healthy_stop(stop)

    def set_o_over(self, start, mid, stop):
        self.set_o_over_start(start)
        self.set_o_over_mid(mid)
        self.set_o_over_stop(stop)

    def set_o_obese(self, start , mid, stop):
        self.set_o_obese_start(start)
        self.set_o_obese_mid(mid)
        self.set_o_obese_stop(stop)

    def set_o(self, healthy_start, healthy_mid, healthy_stop, over_start, over_mid, over_stop, obese_start, obese_mid, obese_stop):
        self.set_o_healthy(healthy_start, healthy_mid, healthy_stop)
        self.set_o_over(over_start, over_mid, over_stop)
        self.set_o_obese(obese_start, obese_mid, obese_stop)

    def make_rules(self):
        """
            step 3: create fuzzy rules
        :return:
        """
        rule1 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['low'] & self.__wc['small'], self.__obesity['healthy'])
        rule2 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['low'] & self.__wc['medium'], self.__obesity['healthy'])
        rule3 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['low'] & self.__wc['large'], self.__obesity['healthy'])
        rule4 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['normal'] & self.__wc['small'], self.__obesity['healthy'])
        rule5 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['normal'] & self.__wc['medium'], self.__obesity['overweight'])
        rule6 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['normal'] & self.__wc['large'], self.__obesity['obese'])
        rule7 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['high'] & self.__wc['small'], self.__obesity['healthy'])
        rule8 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['high'] & self.__wc['medium'], self.__obesity['overweight'])
        rule9 = skfuzzy.control.Rule(self.__bmi['low'] & self.__bf['high'] & self.__wc['large'], self.__obesity['obese'])
        rule10 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['low'] & self.__wc['small'], self.__obesity['healthy'])
        rule11 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['low'] & self.__wc['medium'], self.__obesity['healthy'])
        rule12 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['low'] & self.__wc['large'], self.__obesity['obese'])
        rule13 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['normal'] & self.__wc['small'], self.__obesity['overweight'])
        rule14 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['normal'] & self.__wc['medium'], self.__obesity['overweight'])
        rule15 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['normal'] & self.__wc['large'], self.__obesity['obese'])
        rule16 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['high'] & self.__wc['small'], self.__obesity['overweight'])
        rule17 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['high'] & self.__wc['medium'], self.__obesity['obese'])
        rule18 = skfuzzy.control.Rule(self.__bmi['moderate'] & self.__bf['high'] & self.__wc['large'], self.__obesity['obese'])
        rule19 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['low'] & self.__wc['small'], self.__obesity['healthy'])
        rule20 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['low'] & self.__wc['medium'], self.__obesity['healthy'])
        rule21 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['low'] & self.__wc['large'], self.__obesity['overweight'])
        rule22 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['normal'] & self.__wc['small'], self.__obesity['overweight'])
        rule23 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['normal'] & self.__wc['medium'], self.__obesity['obese'])
        rule24 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['normal'] & self.__wc['large'], self.__obesity['obese'])
        rule25 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['high'] & self.__wc['small'], self.__obesity['overweight'])
        rule26 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['high'] & self.__wc['medium'], self.__obesity['obese'])
        rule27 = skfuzzy.control.Rule(self.__bmi['high'] & self.__bf['high'] & self.__wc['large'], self.__obesity['obese'])
        """
            step 4: create a control system
        """
        self.__rules = []
        for i in range(1, 28):
            self.__rules.append(eval("rule" + str(i)))
        self.__obesity_ctrl = skfuzzy.control.ControlSystem(self.__rules)
        self.__obesity.view()
        input()


    def make_variables(self):
        """
            step 1: create input, output variables
        :return:
        """
        self.__bmi = skfuzzy.control.Antecedent(np.arange(self.__bmi_start, self.__bmi_stop), 'BMI')  # input variable bmi
        self.__bf = skfuzzy.control.Antecedent(np.arange(self.__bf_start, self.__bf_stop), 'BF')  # input variable bf
        self.__wc = skfuzzy.control.Antecedent(np.arange(self.__wc_start, self.__wc_stop), 'WC')  # input variable wc
        self.__obesity = skfuzzy.control.Consequent(np.arange(self.__o_start, self.__o_stop), 'OL')  # output variable OL = Obesity Level


    def make_member_functions(self):
        """
            step 2: create member functions
        :return:
        """
        self.__bmi['low'] = fuzz.trimf(self.__bmi.universe, [self.__bmi_low_start, self.__bmi_low_mid, self.__bmi_low_stop])
        self.__bmi['moderate'] = fuzz.trimf(self.__bmi.universe, [self.__bmi_mod_start, self.__bmi_mod_mid, self.__bmi_mod_stop])
        self.__bmi['high'] = fuzz.trimf(self.__bmi.universe, [self.__bmi_high_start, self.__bmi_high_mid, self.__bmi_high_stop])
        self.__bf['low'] = fuzz.trimf(self.__bf.universe, [self.__bf_low_start, self.__bf_low_mid, self.__bf_low_stop])
        self.__bf['normal'] = fuzz.trimf(self.__bf.universe, [self.__bf_nor_start, self.__bf_nor_mid, self.__bf_nor_stop])
        self.__bf['high'] = fuzz.trimf(self.__bf.universe, [self.__bf_high_start, self.__bf_high_mid, self.__bf_high_stop])
        self.__wc['small'] = fuzz.trimf(self.__wc.universe, [self.__wc_small_start, self.__wc_small_mid, self.__wc_small_stop])
        self.__wc['medium'] = fuzz.trimf(self.__wc.universe, [self.__wc_med_start, self.__wc_med_mid, self.__wc_med_stop])
        self.__wc['large'] = fuzz.trimf(self.__wc.universe, [self.__wc_large_start, self.__wc_large_mid, self.__wc_large_stop])
        self.__obesity['healthy'] = fuzz.trimf(self.__obesity.universe, [self.__o_healthy_start, self.__o_healthy_mid, self.__o_healthy_stop])
        self.__obesity['overweight'] = fuzz.trimf(self.__obesity.universe, [self.__o_over_start, self.__o_over_mid, self.__o_over_stop])
        self.__obesity['obese'] = fuzz.trimf(self.__obesity.universe, [self.__o_obese_start, self.__o_obese_mid, self.__o_obese_stop])


    def simulate(self, bmi_val, bf_val, wc_val):
        """
        :param bmi_val: body mass index value , int or float
        :param bf_val: body fat value, int or float
        :param wc_val: waist circuference value, int or float
        :return: res: a string store step by step instructions how the fuzzy controler infer
        res is stored in result.txt
        """
        obesity_ctrl_sil = skfuzzy.control.ControlSystemSimulation(self.__obesity_ctrl)
        obesity_ctrl_sil.input['BMI'] = bmi_val
        obesity_ctrl_sil.input['BF'] = bf_val
        obesity_ctrl_sil.input['WC'] = wc_val
        obesity_ctrl_sil.compute()
        obesity_ctrl_sil.print_state()

        def get_result():
            file = open("result.txt", "r")
            return file.read()
        return get_result()

if __name__ == '__main__':
    fuzzy_system = FuzzySystem(0, 35, 0, 35, 0, 120, 0, 100)
    fuzzy_system.set_bmi(0, 15, 22, 15, 22, 29, 22, 29, 35)
    fuzzy_system.set_bf(0, 15, 22, 15, 22, 29, 22, 29, 35)
    fuzzy_system.set_wc(0, 30, 60, 30, 60, 90, 60, 90, 120)
    fuzzy_system.set_o(0, 20, 40, 30, 50, 70, 60, 80, 100)
    fuzzy_system.make_variables()
    fuzzy_system.make_member_functions()
    fuzzy_system.make_rules()

    print(fuzzy_system.simulate(26, 26, 70))




