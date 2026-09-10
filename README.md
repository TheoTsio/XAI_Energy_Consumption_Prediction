# XAI_Energy_Consumption_Prediction



\begin{table}[htbp]
\caption{Experiments with features from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.5003 & 0.3967 & 0.6299 & 0.1021 & 0.8315 \\
\hline
MLP & 0.5435 & 0.4317 & 0.6570 & 0.1065 & 0.8167\\
\hline
LightGBM & 0.3167 & 0.1630 & 0.4038 & 0.0655 & 0.9237 \\
\hline
Gradient Boost & 0.3225 & 0.1702 & 0.4125 & 0.0669 & 0.9204 \\
\hline
XGBOOST  & 0.3181 & 0.1673 & 0.4090 & 0.0663 & 0.9217  \\
\hline
RNN - LSTM & 0.4329 & 0.3118 & 0.5584 & 0.0906 & 0.8676\\
\hline
\multicolumn{6}{l}{$^{\mathrm{a}}$Sample of a Table footnote.}
\end{tabular}
\end{table}


\begin{table}[htbp]
\caption{Experiments with features from all the sensors for \textbf{South} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.6185 & 0.9925 & 0.9962 & 0.1314 & 0.7642 \\
\hline
MLP & 0.7950 & 1.0949 & 1.0464 & 0.1380 & 0.7398 \\
\hline
LightGBM & 0.2021 & 0.1528 & 0.3909 & 0.0516 & 0.9598 \\
\hline
Gradient Boost & 0.2011 & 0.1464 & 0.3826 & 0.0505 & 0.9615 \\
\hline
XGBOOST & 0.2087 & 0.1511 & 0.3887 & 0.0513 & 0.9603 \\
\hline
RNN - LSTM & 0.4038 & 0.5119 & 0.7155 & 0.0944 & 0.8784 \\
\hline
\multicolumn{6}{l}{$^{\mathrm{a}}$Sample of a Table footnote.}
\end{tabular}
\end{table}

\begin{table}[htbp]
\caption{Experiments with only \textbf{CO2} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.6197 & 0.6518 & 0.8073 & 0.1309 &  0.7232\\
\hline
MLP & 0.4976 & 0.3958 & 0.6291 & 0.1020  & 0.8319 \\
\hline
LightGBM & 0.4315 & 0.2765 & 0.5259 & 0.0853 & 0.8706 \\
\hline
Gradient Boost & 0.4372 & 0.2888 & 0.5374 & 0.0871 & 0.8649 \\
\hline
XGBOOST & 0.4380 & 0.2854 & 0.5342 & 0.0866 & 0.8665 \\
\hline
RNN - LSTM & 0.4203 & 0.3483 & 0.5901 & 0.0957 & 0.8521 \\
\hline
\multicolumn{6}{l}{$^{\mathrm{a}}$Sample of a Table footnote.}
\end{tabular}
\end{table}

\begin{table}[htbp]
\caption{Experiments with only \textbf{HUM} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.4578 & 0.3265 & 0.5714 & 0.0927 & 0.8614 \\
\hline
MLP & 0.4105 & 0.2842 & 0.5331 & 0.0865 & 0.8793 \\
\hline
LightGBM & 0.5456 & 0.4202 & 0.6482 & 0.1051 & 0.8034 \\
\hline
Gradient Boost & 0.5797 & 0.4729 & 0.6877 & 0.1115 & 0.7787 \\
\hline
XGBOOST & 0.5196 & 0.3961 & 0.6294 & 0.1021 & 0.8146 \\
\hline
RNN - LSTM & 0.4082 & 0.2867 & 0.5355 & 0.0868 & 0.8782 \\
\hline
\multicolumn{6}{l}{}
\end{tabular}
\end{table}


\begin{table}[htbp]
\caption{Experiments with only \textbf{TMP} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.4470 & 0.3193 & 0.5651 & 0.0916 & 0.8644 \\
\hline
MLP & 0.5543 & 0.4432 & 0.6657 & 0.1080 & 0.8118 \\
\hline
LightGBM & 0.4498 & 0.3144 & 0.5607 & 0.0909 & 0.8529 \\
\hline
Gradient Boost & 0.4517 & 0.3204 & 0.5660 & 0.0918 & 0.8501 \\
\hline
XGBOOST & 0.4259 & 0.2939 & 0.5421 & 0.0879 & 0.8625 \\
\hline
RNN - LSTM & 0.4380 & 0.3639 & 0.6033 & 0.0978 & 0.8454 \\
\hline
\multicolumn{6}{l}{}
\end{tabular}
\end{table}


\begin{table}[htbp]
\caption{Experiments with only \textbf{VOCT} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.4398 & 0.3748 & 0.6122 & 0.0993 & 0.8408 \\
\hline
MLP & 0.4462 & 0.3902 & 0.6247 & 0.1013 & 0.8343 \\
\hline
LightGBM & 0.4933 & 0.3678 & 0.6064 & 0.0983 & 0.8279 \\
\hline
Gradient Boost & 0.5230 & 0.4198 & 0.6479 & 0.1051 & 0.8036 \\
\hline
XGBOOST & 0.5131 & 0.3947 & 0.6282 & 0.1019 & 0.8153 \\
\hline
RNN - LSTM & 0.4247 & 0.3607 & 0.6006 & 0.0974 & 0.8468 \\
\hline
\multicolumn{6}{l}{}
\end{tabular}
\end{table}

\begin{table}[htbp]
\caption{Experiments with only \textbf{DBAA} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.3910 & 0.2743 & 0.5238 & 0.0849 & 0.8835 \\
\hline
MLP & 0.3622 & 0.2334 & 0.4832 & 0.0784 & 0.9009 \\
\hline
LightGBM & 0.3552 & 0.1992 & 0.4463 & 0.0724 & 0.9068 \\
\hline
Gradient Boost & 0.3636 & 0.2094 & 0.4576 & 0.0742 & 0.9020 \\
\hline
XGBOOST & 0.3584 & 0.2018 & 0.4492 & 0.0728 & 0.9056 \\
\hline
RNN - LSTM & 0.3380 & 0.2119 & 0.4603 & 0.0746 & 0.9100 \\
\hline
\multicolumn{6}{l}{}
\end{tabular}
\end{table}

\begin{table}[htbp]
\caption{Experiments with only \textbf{LIGHT LUX} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.4230 & 0.3638 & 0.6032 & 0.0978 & 0.8455 \\
\hline
MLP & 0.5075 & 0.4042 & 0.6358 & 0.1031 & 0.8283 \\
\hline
LightGBM & 0.4319 & 0.2847 & 0.5336 & 0.0865 & 0.8667 \\
\hline
Gradient Boost & 0.4298 & 0.2901 & 0.5386 & 0.0873 & 0.8643 \\
\hline
XGBOOST & 0.4264 & 0.2803 & 0.5294 & 0.0859 & 0.8688 \\
\hline
RNN - LSTM & 0.4277 & 0.3073 & 0.5544 & 0.0899 & 0.8695\\
\hline
\multicolumn{6}{l}{}
\end{tabular}
\end{table}

\begin{table}[htbp]
\caption{Experiments with only \textbf{Occupancy Rate} from all the sensors for \textbf{North} Building }
\label{tab1}
\centering
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{\textit{MAE}} & \textbf{\textit{MSE}} & \textbf{\textit{RMSE}} & \textbf{\textit{NRMSE}} & \textbf{$R^2$} \\
\hline
CNN & 0.3929 & 0.3132 & 0.5597 & 0.0908 & 0.8670 \\
\hline
MLP & 0.3772 & 0.2902 & 0.5387 & 0.0874 & 0.8768 \\
\hline
LightGBM & 0.4125 & 0.2683 & 0.5180 & 0.0840 & 0.8744 \\
\hline
Gradient Boost & 0.4223 & 0.2907 & 0.5391 & 0.0874 & 0.8640 \\
\hline
XGBOOST & 0.4141 & 0.2735 & 0.5230 & 0.0848 & 0.8720 \\
\hline
RNN - LSTM & 0.3868 & 0.2898 & 0.5383 & 0.0873 & 0.8769 \\
\hline
\multicolumn{6}{l}{}
\end{tabular}
\end{table}