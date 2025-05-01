ggplot() +
    geom_vline(data = vacc_data %>% rename(xx = x), aes(xintercept = date, color = xx)) +
    geom_line(data = data_gesamt %>% filter(grepl("Fälle gesamt", x) | grepl("Anteil Verstorben", x)),
      aes(x = date, y = y, color = x)) +
scale_x_date(date_breaks = "1 month",
             date_minor_breaks = "1 week") +
    facet_grid(x ~ ., scales = "free") +
    ggrepel::geom_label_repel(data = vacc_data %>% rename(xx = x),
      aes(x = date, y = 7, label = label, color = xx),
      arrow = arrow(length = unit(0.02, "npc"))) +
theme(legend.position="top")


ggplot() +
    geom_vline(data = vacc_data,
      aes(xintercept = date, color = x)) +
    geom_line(data = data_gesamt_prep,
      aes(x = date, y = y, color = x, linetype = stat)) +
scale_x_date(date_breaks = "1 month",
      date_minor_breaks = "1 week") +
    ggrepel::geom_label_repel(data = vacc_data,
       aes(x = date, y = 90, label = label, color = x),
       arrow = arrow(length = unit(0.02, "npc"))) +
theme(legend.position="top")

ggplot() +
    geom_vline(data = vacc_data %>% rename(xx = x), aes(xintercept = date, color = xx)) +
    geom_line(data = data_gesamt %>% filter(grepl("Frauen", x)),
      aes(x = date, y = y, color = x)) +
scale_x_date(date_breaks = "1 month",
      date_minor_breaks = "1 week") +
    ggrepel::geom_label_repel(data = vacc_data %>% rename(xx = x),
      aes(x = date, y = 56, label = label, color = xx),
      arrow = arrow(length = unit(0.02, "npc"))) +
theme(legend.position="top")