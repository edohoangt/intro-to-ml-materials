Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:\OneDrive\current-month-workspace\apr\intro-to-ml-mit-ex\week3\code_and_data_for_hw3\code_and_data_for_hw3\hw3_part2_main.py
Importing code_for_hw03 (part 2, imported as hw3)
Imported tidy_plot, plot_separator, plot_data, plot_nonlin_sep, cv, rv, y, positive, score
         xval_learning_alg, eval_classifier
Tests: test_linear_classifier
Dataset tools: load_auto_data, std_vals, standard, raw, one_hot, auto_data_and_labels
               load_review_data, clean, extract_words, bag_of_words, extract_bow_feature_vectors
               load_mnist_data, load_mnist_single
avg and std {'displacement': (388.3482142857143, 302.0458123396403), 'horsepower': (509.3545918367347, 333.6521151716361), 'weight': (2977.5841836734694, 848.3184465698365), 'acceleration': (15.541326530612228, 2.7553429127509963)}
entries in one_hot field {'cylinders': [3.0, 4.0, 5.0, 6.0, 8.0], 'origin': [1.0, 2.0, 3.0]}
auto data and labels shape (12, 392) (1, 392)
review_bow_data and labels shape (19945, 10000) (1, 10000)
mnist_data_all loaded. shape of single images is (28, 28)
data.shape
(160, 28, 28)
labels.shape
(1, 160)
for i in data.shape[0]:
    np.reshape(data[i], (28*28,))
    .
    
SyntaxError: invalid syntax
for i in data.shape[0]:
    np.reshape(data[i], (28*28,))

    
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for i in data.shape[0]:
TypeError: 'int' object is not iterable
data[i]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data[i]
NameError: name 'i' is not defined. Did you mean: 'id'?
data[0]
array([[0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 1.5378701e-04, 1.5378702e-05, 0.0000000e+00,
        6.1514809e-05, 0.0000000e+00, 0.0000000e+00, 1.2302962e-04,
        0.0000000e+00, 6.1514809e-05, 1.2302962e-04, 1.5378702e-05,
        0.0000000e+00, 1.6916571e-04, 1.5378702e-05, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        1.9992310e-04, 0.0000000e+00, 0.0000000e+00, 2.7681663e-04,
        0.0000000e+00, 0.0000000e+00, 3.0757402e-04, 0.0000000e+00,
        1.6916571e-04, 0.0000000e+00, 0.0000000e+00, 3.0757405e-05,
        1.3840832e-04, 0.0000000e+00, 0.0000000e+00, 1.3840832e-04,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 7.6893506e-05, 0.0000000e+00, 0.0000000e+00,
        6.1514809e-05, 0.0000000e+00, 0.0000000e+00, 9.2272203e-05,
        0.0000000e+00, 1.8454441e-04, 9.2272203e-05, 0.0000000e+00,
        1.2302962e-04, 6.1514809e-05, 1.5378702e-05, 4.6136101e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        1.5378702e-05, 0.0000000e+00, 9.2272203e-05, 9.2272203e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        7.6893506e-05, 0.0000000e+00, 0.0000000e+00, 1.9992310e-04,
        0.0000000e+00, 0.0000000e+00, 1.0765091e-04, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 4.6136101e-05,
        1.0765091e-04, 0.0000000e+00, 1.0765091e-04, 8.6120726e-04,
        2.5528644e-03, 3.9215689e-03, 2.4144561e-03, 8.6120726e-04,
        0.0000000e+00, 3.5371011e-04, 0.0000000e+00, 1.5378702e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 3.2295272e-04, 0.0000000e+00, 0.0000000e+00,
        1.0765091e-04, 0.0000000e+00, 9.0734335e-04, 3.3833142e-03,
        3.5986160e-03, 3.9215689e-03, 3.8600538e-03, 3.7831604e-03,
        7.6893506e-05, 0.0000000e+00, 1.0765091e-04, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        1.2302962e-04, 0.0000000e+00, 1.0765091e-04, 1.5378701e-04,
        0.0000000e+00, 1.0611304e-03, 3.1218762e-03, 3.9215689e-03,
        3.9215689e-03, 3.8139177e-03, 3.3064208e-03, 3.7831604e-03,
        8.6120726e-04, 1.3840832e-04, 1.5378701e-04, 6.1514809e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 7.6893506e-05,
        1.0918878e-03, 3.1064975e-03, 3.9215689e-03, 3.7062669e-03,
        3.8446751e-03, 2.8296809e-03, 1.6301422e-03, 3.9061899e-03,
        3.9061899e-03, 1.9223376e-03, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 7.6893506e-05, 0.0000000e+00, 0.0000000e+00,
        1.9992310e-04, 0.0000000e+00, 0.0000000e+00, 6.1514809e-05,
        1.0765091e-04, 0.0000000e+00, 1.2302962e-04, 2.6451366e-03,
        3.6139947e-03, 3.9215689e-03, 3.9215689e-03, 3.9215689e-03,
        3.9215689e-03, 3.6139947e-03, 1.6916571e-03, 2.8911957e-03,
        3.8139177e-03, 2.6912726e-03, 7.6893506e-05, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 7.6893506e-05, 0.0000000e+00, 0.0000000e+00,
        6.1514809e-05, 0.0000000e+00, 0.0000000e+00, 3.0757405e-05,
        9.2272203e-05, 6.1514809e-05, 7.6893502e-04, 3.6755095e-03,
        3.9215689e-03, 3.7370243e-03, 2.9065744e-03, 1.6147635e-03,
        3.9215689e-03, 3.5217225e-03, 6.1514805e-04, 1.2302961e-03,
        3.9215689e-03, 2.4298348e-03, 1.0765091e-04, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [1.5378702e-05, 3.0757405e-05, 1.5378702e-05, 0.0000000e+00,
        0.0000000e+00, 1.5378702e-05, 1.5378702e-05, 0.0000000e+00,
        1.3840832e-04, 4.3060363e-04, 3.5832373e-03, 3.9215689e-03,
        3.7524030e-03, 3.0142253e-03, 1.0765091e-04, 1.2764322e-03,
        1.6455210e-03, 5.2287587e-04, 1.5378702e-05, 3.0757405e-05,
        3.9215689e-03, 3.5986160e-03, 8.1507111e-04, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 6.1514809e-05, 0.0000000e+00,
        0.0000000e+00, 6.1514809e-05, 0.0000000e+00, 0.0000000e+00,
        5.5363326e-04, 2.6451366e-03, 3.9215689e-03, 3.4140716e-03,
        3.3525568e-03, 1.2764322e-03, 0.0000000e+00, 0.0000000e+00,
        1.0765091e-04, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        3.9215689e-03, 3.8600538e-03, 2.5528644e-03, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 7.6893506e-05, 1.5378702e-05,
        1.5378702e-05, 0.0000000e+00, 0.0000000e+00, 1.8454441e-04,
        2.7374087e-03, 3.9061899e-03, 3.4909651e-03, 1.2149174e-03,
        1.9992310e-04, 1.6916571e-04, 1.8454441e-04, 1.0765091e-04,
        0.0000000e+00, 3.8446751e-04, 0.0000000e+00, 0.0000000e+00,
        3.9215689e-03, 3.8292964e-03, 2.9219531e-03, 9.2272203e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [3.0757405e-05, 0.0000000e+00, 6.1514809e-05, 0.0000000e+00,
        1.5378702e-05, 0.0000000e+00, 0.0000000e+00, 1.1226452e-03,
        3.9061899e-03, 3.8139177e-03, 9.6885813e-04, 2.3068051e-04,
        0.0000000e+00, 3.0757402e-04, 4.6136101e-05, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 1.5378701e-04,
        3.7831604e-03, 3.9215689e-03, 2.7989235e-03, 9.2272203e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [6.1514809e-05, 0.0000000e+00, 3.0757405e-05, 0.0000000e+00,
        3.0757405e-05, 0.0000000e+00, 4.6136102e-04, 2.6912726e-03,
        3.8754325e-03, 2.9988466e-03, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 4.1522493e-04,
        2.4605924e-04, 0.0000000e+00, 0.0000000e+00, 2.4605924e-04,
        3.7831604e-03, 3.6447521e-03, 3.1526336e-03, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [4.6136101e-05, 0.0000000e+00, 1.5378702e-05, 0.0000000e+00,
        6.1514809e-05, 0.0000000e+00, 9.8423695e-04, 3.9215689e-03,
        3.9061899e-03, 1.6608997e-03, 1.3840832e-04, 0.0000000e+00,
        3.0757405e-05, 1.5378701e-04, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 6.1514809e-05, 2.7681663e-04, 0.0000000e+00,
        3.9215689e-03, 3.9215689e-03, 2.0761248e-03, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [4.6136101e-05, 4.6136101e-05, 1.5378702e-05, 0.0000000e+00,
        1.5378702e-05, 9.2272203e-05, 1.3687044e-03, 3.8139177e-03,
        3.5371012e-03, 3.9984621e-04, 4.6136101e-05, 0.0000000e+00,
        7.6893506e-05, 7.6893506e-05, 1.5378701e-04, 0.0000000e+00,
        1.5378702e-05, 0.0000000e+00, 1.6916571e-04, 1.9684739e-03,
        3.8754325e-03, 2.8450596e-03, 2.9219533e-04, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [1.5378702e-05, 0.0000000e+00, 6.1514809e-05, 1.0765091e-04,
        6.1514809e-05, 0.0000000e+00, 1.2149174e-03, 3.9061899e-03,
        3.4294503e-03, 2.3068051e-04, 0.0000000e+00, 0.0000000e+00,
        4.6136101e-05, 0.0000000e+00, 0.0000000e+00, 1.5378702e-05,
        1.0765091e-04, 0.0000000e+00, 2.0299887e-03, 3.9215689e-03,
        3.5986160e-03, 9.8423695e-04, 0.0000000e+00, 3.0757405e-05,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [4.6136101e-05, 3.0757405e-05, 3.0757405e-05, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 1.3379470e-03, 3.9215689e-03,
        2.1991543e-03, 0.0000000e+00, 3.0757405e-05, 0.0000000e+00,
        1.5378701e-04, 1.6916571e-04, 0.0000000e+00, 4.6136101e-05,
        5.9976935e-04, 2.9527105e-03, 3.8292964e-03, 2.2914265e-03,
        7.6893506e-05, 1.2302962e-04, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 7.6893506e-05, 6.1514809e-05, 0.0000000e+00,
        0.0000000e+00, 9.2272203e-05, 1.3994618e-03, 3.7985391e-03,
        3.3525568e-03, 3.6908881e-04, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 2.1530181e-04, 1.7070358e-03,
        3.6139947e-03, 3.8908112e-03, 2.5682431e-03, 0.0000000e+00,
        6.1514809e-05, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 1.5378702e-05, 1.0765091e-04, 4.6136101e-05,
        1.5378702e-05, 1.5378702e-05, 1.2764322e-03, 3.7677817e-03,
        3.8600538e-03, 1.9377163e-03, 1.0303730e-03, 3.3833142e-04,
        1.2610535e-03, 2.8604383e-03, 3.5063438e-03, 3.7677817e-03,
        3.5217225e-03, 2.4605922e-03, 8.7658595e-04, 2.3068051e-04,
        0.0000000e+00, 2.7681663e-04, 0.0000000e+00, 1.0765091e-04,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [6.1514809e-05, 0.0000000e+00, 0.0000000e+00, 7.6893506e-05,
        3.0757405e-05, 0.0000000e+00, 1.2610535e-03, 3.9215689e-03,
        3.9215689e-03, 3.6293734e-03, 3.5217225e-03, 3.4448290e-03,
        3.8292964e-03, 3.9215689e-03, 3.7370243e-03, 3.1526336e-03,
        2.0453674e-03, 9.2272203e-05, 0.0000000e+00, 0.0000000e+00,
        2.4605924e-04, 0.0000000e+00, 6.1514809e-05, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [9.2272203e-05, 1.5378702e-05, 0.0000000e+00, 0.0000000e+00,
        3.0757405e-05, 0.0000000e+00, 7.6893502e-04, 2.8143022e-03,
        3.6601308e-03, 3.9215689e-03, 3.8446751e-03, 3.6908882e-03,
        3.8600538e-03, 3.5524799e-03, 2.1068822e-03, 4.6136101e-05,
        0.0000000e+00, 6.1514809e-05, 1.6916571e-04, 2.1530181e-04,
        0.0000000e+00, 9.2272203e-05, 0.0000000e+00, 1.0765091e-04,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 1.2302962e-04, 7.6893506e-05, 0.0000000e+00,
        1.5378701e-04, 6.1514809e-05, 0.0000000e+00, 4.9211847e-04,
        2.2299117e-03, 3.6293734e-03, 3.9215689e-03, 3.8446751e-03,
        2.3221839e-03, 4.9211847e-04, 1.2302962e-04, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 7.6893506e-05, 0.0000000e+00,
        0.0000000e+00, 1.0765091e-04, 4.6136101e-05, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00],
       [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
        0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00]],
      dtype=float32)
len(data)
160
for i in len(data):
    np.reshape(data[i], (28*28,))

    
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for i in len(data):
TypeError: 'int' object is not iterable
for i in range(len(data)):
    data[i] = np.reshape(data[i], (28*28,))

    
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    data[i] = np.reshape(data[i], (28*28,))
ValueError: could not broadcast input array from shape (784,) into shape (28,28)
new_data = []
for i in range(len(data)):
    new_data.append(np.reshape(data[i], (28*28,)))

    
new_data.shape
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    new_data.shape
AttributeError: 'list' object has no attribute 'shape'
len(new_data)
160
new_data = np.array(new_data)
new_data.shape
(160, 784)