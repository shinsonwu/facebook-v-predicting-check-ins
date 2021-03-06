import xgboost_extra_features_model as xgbm
import grid_generation as grid

g = grid.Grid(200, 50, 20, 5, pref = 'grid', files_flag=True, train_file='../main_train_0.02_5.csv')
xgbm1 = xgbm.XGB_Model(grid = g, threshold = 7, cross_validation_file='../main_cv_0.02_5.csv')

# feature_submission_name first run = ec2_colsample_bytree0_6_scale_pos_weight1_min_child_weight6_subsample0_9_eta0_1_max_depth3_gamma0_1_th3_n200

if __name__ == '__main__':
    """
    eta = 0.1
    max_depth = 13
    min_child_weight = 5
    gamma = 0.3
    subsample = 0.9
    colsample_bytree = 0.711
{'colsample_bytree': 0.6, 'silent': 1, 'scale_pos_weight': 1, 'nthread': 8, 'min_child_weight': 6, 'subsample': 0.9, 'eta': 0.1, 'objective': 'multi:softprob', 'alpha': 0.005, 'max_depth': 3, 'gamma': 0.1}
    """
    xgbm1.train_and_predict_parallel('../feature_run_th7_n100.csv', upload_to_s3=True)
