% Count the number of ways to make change for a given amount of money.
% 
% * Set value of x to amount of money for which to make change. Default is
% 100 cents.
%
% * For American system (default), use these name-value pairs: 
% 'coinValues',[1 5 10 25]
% 'coinNames',{'Pennies' 'Nickels' 'Dimes' 'Quarters'}
%
% * For British system, use this name-value pair: 
% 'coinValues',[1 2 5 10 20 50]

chartObj = sf_change('x',27,'-warningOnUninitializedData',false);

while ~chartObj.done
    step(chartObj);
end

disp(chartObj.tabula);